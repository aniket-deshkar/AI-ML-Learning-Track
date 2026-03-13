from __future__ import annotations

import json
import logging
import re
from time import monotonic
from typing import Any, Callable

from .models import ClassificationOutput, ProviderHealth, ProviderRuntime

LOGGER = logging.getLogger(__name__)


class MultiProviderLLM:
    def __init__(self, providers: list[ProviderRuntime], cooldown_seconds: float = 30.0) -> None:
        self.providers = providers
        self.cooldown_seconds = cooldown_seconds
        self._preferred_index = 0
        self._health = {self._provider_key(provider): ProviderHealth() for provider in providers}

    def classify(self, text: str) -> tuple[ClassificationOutput, ProviderRuntime]:
        system_prompt = (
            "You classify legal documents. Return strict JSON with keys: "
            "intent, workflow, confidence, rationale. "
            "intent must be one of: contract, compliance_report, vendor_agreement, unknown. "
            "workflow must be one of: summarization, clause_extraction, risk_detection. "
            "confidence must be between 0 and 1."
        )
        return self._execute(
            operation_name="classification",
            prompt_system=system_prompt,
            prompt_user=text[:12_000],
            parser=lambda raw: ClassificationOutput.model_validate(self._parse_json_payload(raw)),
            output_json=True,
        )

    def summarize(self, text: str) -> tuple[str, ProviderRuntime]:
        return self._execute(
            operation_name="summarization",
            prompt_system="Summarize this legal document in 4 concise bullet points.",
            prompt_user=text[:12_000],
            parser=self._validate_summary,
            output_json=False,
        )

    def _execute(
        self,
        operation_name: str,
        prompt_system: str,
        prompt_user: str,
        parser: Callable[[str], Any],
        output_json: bool,
    ) -> tuple[Any, ProviderRuntime]:
        errors: list[str] = []
        for idx, provider in self._ordered_candidates():
            try:
                raw_text = self._dispatch(provider, prompt_system, prompt_user, output_json=output_json)
                parsed = parser(raw_text)
                self._on_success(idx, provider)
                return parsed, provider
            except Exception as exc:  # pragma: no cover - external dependency behavior
                errors.append(f"{provider.name}:{exc}")
                self._on_failure(provider)
                LOGGER.warning(
                    "%s failed on provider=%s model=%s: %s",
                    operation_name.capitalize(),
                    provider.name,
                    provider.model,
                    exc,
                )
        raise RuntimeError(f"All LLM providers failed {operation_name}: {errors}")

    def _dispatch(self, provider: ProviderRuntime, system_prompt: str, user_prompt: str, output_json: bool) -> str:
        if provider.name == "gemini":
            return self._gemini_generate(provider, system_prompt, user_prompt, output_json=output_json)
        if provider.name == "groq":
            return self._groq_generate(provider, system_prompt, user_prompt, output_json=output_json)
        return self._huggingface_generate(provider, system_prompt, user_prompt, output_json=output_json)

    def _ordered_candidates(self) -> list[tuple[int, ProviderRuntime]]:
        now = monotonic()
        start = self._preferred_index if self.providers else 0
        ordered = [
            ((start + offset) % len(self.providers), self.providers[(start + offset) % len(self.providers)])
            for offset in range(len(self.providers))
        ]
        available = [
            (idx, provider)
            for idx, provider in ordered
            if self._health[self._provider_key(provider)].unavailable_until <= now
        ]
        return available if available else ordered

    def _on_success(self, provider_index: int, provider: ProviderRuntime) -> None:
        self._health[self._provider_key(provider)] = ProviderHealth()
        self._preferred_index = provider_index

    def _on_failure(self, provider: ProviderRuntime) -> None:
        health = self._health[self._provider_key(provider)]
        health.consecutive_failures += 1
        if health.consecutive_failures >= 2:
            health.unavailable_until = monotonic() + self.cooldown_seconds
            health.consecutive_failures = 0

    @staticmethod
    def _provider_key(provider: ProviderRuntime) -> str:
        return f"{provider.name}:{provider.model}"

    @staticmethod
    def _gemini_generate(provider: ProviderRuntime, system_prompt: str, user_prompt: str, output_json: bool) -> str:
        prompt = f"{system_prompt}\n\n{user_prompt}"
        config: dict[str, Any] = {"temperature": 0, "max_output_tokens": provider.max_output_tokens}
        if output_json:
            config["response_mime_type"] = "application/json"
        response = provider.client.models.generate_content(model=provider.model, contents=prompt, config=config)
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned empty text response")
        return str(text)

    @staticmethod
    def _groq_generate(provider: ProviderRuntime, system_prompt: str, user_prompt: str, output_json: bool) -> str:
        request: dict[str, Any] = {
            "model": provider.model,
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
            "temperature": 0,
            "max_tokens": provider.max_output_tokens,
        }
        if output_json:
            request["response_format"] = {"type": "json_object"}
        response = provider.client.chat.completions.create(**request)
        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("Groq returned empty text response")
        return str(content)

    @staticmethod
    def _huggingface_generate(provider: ProviderRuntime, system_prompt: str, user_prompt: str, output_json: bool) -> str:
        content_instruction = "Return strict JSON only." if output_json else "Return concise summary text."
        response = provider.client.chat.completions.create(
            model=provider.model,
            messages=[
                {"role": "system", "content": f"{system_prompt} {content_instruction}"},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
            max_tokens=provider.max_output_tokens,
        )
        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("Hugging Face returned empty text response")
        return str(content)

    @staticmethod
    def _validate_summary(text: str) -> str:
        summary = text.strip()
        if not summary:
            raise RuntimeError("Empty summary returned")
        return summary

    @staticmethod
    def _parse_json_payload(payload: str) -> dict[str, Any]:
        cleaned = payload.strip()
        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
            cleaned = re.sub(r"\s*```$", "", cleaned)
        return json.loads(cleaned)
