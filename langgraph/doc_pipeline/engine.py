from __future__ import annotations

import logging
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Any, cast

from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

try:
    from google import genai
except ImportError:  # pragma: no cover - optional dependency at runtime
    genai = None

try:
    from groq import Groq
except ImportError:  # pragma: no cover - optional dependency at runtime
    Groq = None

try:
    from huggingface_hub import InferenceClient
except ImportError:  # pragma: no cover - optional dependency at runtime
    InferenceClient = None

from .llm import MultiProviderLLM
from .models import AuditEvent, ClassificationOutput, PipelineState, ProviderRuntime

LOGGER = logging.getLogger(__name__)


class ClauseExtractionError(RuntimeError):
    """Raised when clause extraction fails and should be retried."""


class DocumentProcessingEngine:
    def __init__(
        self,
        confidence_threshold: float = 0.72,
        max_extraction_attempts: int = 3,
        gemini_model: str = "gemini-2.5-flash",
        groq_model: str = "llama-3.3-70b-versatile",
        huggingface_model: str = "Qwen/Qwen2.5-72B-Instruct",
    ) -> None:
        self.confidence_threshold = confidence_threshold
        self.max_extraction_attempts = max_extraction_attempts
        self._llm = self._build_llm(gemini_model=gemini_model, groq_model=groq_model, huggingface_model=huggingface_model)
        self._graph = self._build_graph()

    @property
    def graph(self):
        return self._graph

    def process_document(self, document_text: str, document_id: str | None = None) -> PipelineState:
        resolved_document_id = document_id or str(uuid.uuid4())
        initial_state: PipelineState = {
            "document_id": resolved_document_id,
            "document_text": document_text,
            "intent": "unknown",
            "confidence": 0.0,
            "selected_workflow": "summarization",
            "status": "received",
            "summary": "",
            "clauses": [],
            "risks": [],
            "llm_provider": "",
            "llm_model": "",
            "extraction_attempts": 0,
            "max_extraction_attempts": self.max_extraction_attempts,
            "clause_extraction_succeeded": False,
            "errors": [],
            "route_history": [],
            "audit_log": [],
        }
        return self._graph.invoke(initial_state, config={"configurable": {"thread_id": resolved_document_id}})

    def get_state_snapshot(self, document_id: str) -> PipelineState | None:
        snapshot = self._graph.get_state({"configurable": {"thread_id": document_id}})
        return None if snapshot.values is None else cast(PipelineState, snapshot.values)

    def _build_llm(self, gemini_model: str, groq_model: str, huggingface_model: str) -> MultiProviderLLM | None:
        providers: list[ProviderRuntime] = []

        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if genai is not None and gemini_api_key:
            providers.append(
                ProviderRuntime(
                    name="gemini",
                    model=os.getenv("GEMINI_MODEL", gemini_model),
                    max_output_tokens=8192,
                    client=genai.Client(api_key=gemini_api_key),
                )
            )

        groq_api_key = os.getenv("GROQ_API_KEY")
        if Groq is not None and groq_api_key:
            providers.append(
                ProviderRuntime(
                    name="groq",
                    model=os.getenv("GROQ_MODEL", groq_model),
                    max_output_tokens=4096,
                    client=Groq(api_key=groq_api_key),
                )
            )

        hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if InferenceClient is not None and hf_token:
            providers.append(
                ProviderRuntime(
                    name="huggingface",
                    model=os.getenv("HF_MODEL", huggingface_model),
                    max_output_tokens=4096,
                    client=InferenceClient(token=hf_token),
                )
            )

        if not providers:
            LOGGER.info("No Gemini/Groq/Hugging Face LLM configured; running in deterministic fallback mode.")
            return None

        cooldown_seconds = float(os.getenv("LLM_PROVIDER_COOLDOWN_SECONDS", "30"))
        provider_order = ", ".join(f"{provider.name}:{provider.model}" for provider in providers)
        LOGGER.info("Configured LLM providers (fallback order): %s", provider_order)
        LOGGER.info("Provider cooldown window: %.1f seconds after repeated failures.", cooldown_seconds)
        return MultiProviderLLM(providers, cooldown_seconds=cooldown_seconds)

    def _build_graph(self):
        graph = StateGraph(PipelineState)
        graph.add_node("normalize_input", self._normalize_input)
        graph.add_node("ingest", self._ingest)
        graph.add_node("classify", self._classify, retry_policy=RetryPolicy(max_attempts=2))
        graph.add_node("manual_review", self._manual_review)
        graph.add_node("summarize", self._summarize, retry_policy=RetryPolicy(max_attempts=2))
        graph.add_node("extract_clauses", self._extract_clauses)
        graph.add_node("prepare_clause_retry", self._prepare_clause_retry)
        graph.add_node("risk_detect", self._risk_detect)
        graph.add_node("recover_clause_failure", self._recover_clause_failure)
        graph.add_node("finalize", self._finalize)

        graph.add_edge(START, "normalize_input")
        graph.add_edge("normalize_input", "ingest")
        graph.add_edge("ingest", "classify")
        graph.add_conditional_edges(
            "classify",
            self._route_from_classification,
            {
                "manual_review": "manual_review",
                "summarization": "summarize",
                "clause_extraction": "extract_clauses",
                "risk_detection": "risk_detect",
            },
        )
        graph.add_edge("manual_review", "finalize")
        graph.add_edge("summarize", "finalize")
        graph.add_edge("risk_detect", "finalize")
        graph.add_conditional_edges(
            "extract_clauses",
            self._route_from_clause_extraction,
            {"retry": "prepare_clause_retry", "recover": "recover_clause_failure", "done": "finalize"},
        )
        graph.add_edge("prepare_clause_retry", "extract_clauses")
        graph.add_edge("recover_clause_failure", "finalize")
        graph.add_edge("finalize", END)
        # LangGraph API/Studio manages persistence automatically.
        return graph.compile()

    def _normalize_input(self, state: PipelineState) -> dict[str, Any]:
        incoming_text = state.get("document_text") if isinstance(state, dict) else None
        normalized_text = incoming_text.strip() if isinstance(incoming_text, str) else ""
        incoming_document_id = state.get("document_id") if isinstance(state, dict) else None
        normalized_document_id = (
            incoming_document_id.strip() if isinstance(incoming_document_id, str) and incoming_document_id.strip() else str(uuid.uuid4())
        )

        return {
            "document_id": normalized_document_id,
            "document_text": normalized_text,
            "intent": state.get("intent", "unknown") if isinstance(state, dict) else "unknown",
            "confidence": state.get("confidence", 0.0) if isinstance(state, dict) else 0.0,
            "selected_workflow": state.get("selected_workflow", "summarization") if isinstance(state, dict) else "summarization",
            "status": state.get("status", "received") if isinstance(state, dict) else "received",
            "summary": state.get("summary", "") if isinstance(state, dict) else "",
            "clauses": state.get("clauses", []) if isinstance(state, dict) else [],
            "risks": state.get("risks", []) if isinstance(state, dict) else [],
            "llm_provider": state.get("llm_provider", "") if isinstance(state, dict) else "",
            "llm_model": state.get("llm_model", "") if isinstance(state, dict) else "",
            "extraction_attempts": state.get("extraction_attempts", 0) if isinstance(state, dict) else 0,
            "max_extraction_attempts": state.get("max_extraction_attempts", self.max_extraction_attempts) if isinstance(state, dict) else self.max_extraction_attempts,
            "clause_extraction_succeeded": state.get("clause_extraction_succeeded", False) if isinstance(state, dict) else False,
            "errors": state.get("errors", []) if isinstance(state, dict) else [],
            "route_history": state.get("route_history", []) if isinstance(state, dict) else [],
            "audit_log": state.get("audit_log", []) if isinstance(state, dict) else [],
        }

    def _ingest(self, state: PipelineState) -> dict[str, Any]:
        return {
            "status": "processing",
            "route_history": ["ingest"],
            "audit_log": [self._audit("ingest", "Document ingested", chars=len(state["document_text"]))],
        }

    def _classify(self, state: PipelineState) -> dict[str, Any]:
        output, provider_name, provider_model = self._classify_document(state["document_text"])
        return {
            "intent": output.intent,
            "confidence": output.confidence,
            "selected_workflow": output.workflow,
            "llm_provider": provider_name,
            "llm_model": provider_model,
            "route_history": ["classify"],
            "audit_log": [
                self._audit(
                    "classify",
                    "Document classified",
                    intent=output.intent,
                    workflow=output.workflow,
                    confidence=output.confidence,
                    rationale=output.rationale,
                    llm_provider=provider_name,
                    llm_model=provider_model,
                )
            ],
        }

    def _manual_review(self, state: PipelineState) -> dict[str, Any]:
        return {
            "status": "needs_review",
            "errors": [f"Low-confidence classification ({state['confidence']:.2f}); document routed to manual review."],
            "route_history": ["manual_review"],
            "audit_log": [self._audit("manual_review", "Confidence below threshold", threshold=self.confidence_threshold)],
        }

    def _summarize(self, state: PipelineState) -> dict[str, Any]:
        summary, provider_name, provider_model = self._summarize_text(state["document_text"])
        return {
            "summary": summary,
            "llm_provider": provider_name,
            "llm_model": provider_model,
            "route_history": ["summarize"],
            "audit_log": [
                self._audit(
                    "summarize",
                    "Summary generated",
                    summary_length=len(summary),
                    llm_provider=provider_name,
                    llm_model=provider_model,
                )
            ],
        }

    def _extract_clauses(self, state: PipelineState) -> dict[str, Any]:
        attempt = state["extraction_attempts"] + 1
        try:
            clauses = self._extract_clause_candidates(state["document_text"])
            return {
                "clauses": clauses,
                "clause_extraction_succeeded": True,
                "extraction_attempts": attempt,
                "route_history": ["extract_clauses"],
                "audit_log": [self._audit("extract_clauses", "Clause extraction succeeded", attempt=attempt, clauses_found=len(clauses))],
            }
        except ClauseExtractionError as exc:
            return {
                "clause_extraction_succeeded": False,
                "extraction_attempts": attempt,
                "errors": [f"Clause extraction failed on attempt {attempt}: {exc}"],
                "route_history": ["extract_clauses"],
                "audit_log": [
                    self._audit(
                        "extract_clauses",
                        "Clause extraction failed",
                        attempt=attempt,
                        max_attempts=state["max_extraction_attempts"],
                        error=str(exc),
                    )
                ],
            }

    def _prepare_clause_retry(self, state: PipelineState) -> dict[str, Any]:
        return {
            "route_history": ["prepare_clause_retry"],
            "audit_log": [self._audit("prepare_clause_retry", "Retrying clause extraction", next_attempt=state["extraction_attempts"] + 1)],
        }

    def _risk_detect(self, state: PipelineState) -> dict[str, Any]:
        risks = self._detect_risks(state["document_text"])
        return {
            "risks": risks,
            "route_history": ["risk_detect"],
            "audit_log": [self._audit("risk_detect", "Risk detection completed", risks_found=len(risks))],
        }

    def _recover_clause_failure(self, state: PipelineState) -> dict[str, Any]:
        fallback_summary, provider_name, provider_model = self._summarize_text(state["document_text"])
        return {
            "summary": fallback_summary,
            "llm_provider": provider_name,
            "llm_model": provider_model,
            "status": "needs_review",
            "route_history": ["recover_clause_failure"],
            "audit_log": [
                self._audit(
                    "recover_clause_failure",
                    "Moved to recovery after retries exhausted",
                    attempts=state["extraction_attempts"],
                    llm_provider=provider_name,
                    llm_model=provider_model,
                )
            ],
        }

    @staticmethod
    def _finalize(state: PipelineState) -> dict[str, Any]:
        final_status = "completed" if state["status"] == "processing" else state["status"]
        return {
            "status": final_status,
            "route_history": ["finalize"],
            "audit_log": [DocumentProcessingEngine._audit("finalize", "Pipeline completed", status=final_status)],
        }

    def _route_from_classification(self, state: PipelineState) -> str:
        return "manual_review" if state["confidence"] < self.confidence_threshold else state["selected_workflow"]

    @staticmethod
    def _route_from_clause_extraction(state: PipelineState) -> str:
        if state["clause_extraction_succeeded"]:
            return "done"
        if state["extraction_attempts"] < state["max_extraction_attempts"]:
            return "retry"
        return "recover"

    def _classify_document(self, text: str) -> tuple[ClassificationOutput, str, str]:
        if self._llm is not None:
            try:
                output, provider = self._llm.classify(text)
                return output, provider.name, provider.model
            except Exception as exc:  # pragma: no cover - external dependency behavior
                LOGGER.warning("LLM classification failed across providers, using fallback rules: %s", exc)
        return self._classify_with_rules(text), "rule-engine", "deterministic-v1"

    @staticmethod
    def _classify_with_rules(text: str) -> ClassificationOutput:
        lowered = text.lower()
        if any(token in lowered for token in ("regulation", "compliance", "non-compliance", "audit finding", "penalty")):
            return ClassificationOutput(intent="compliance_report", workflow="risk_detection", confidence=0.86, rationale="Compliance-oriented terms detected.")
        if any(token in lowered for token in ("vendor", "supplier", "procurement", "service level", "purchase order")):
            return ClassificationOutput(intent="vendor_agreement", workflow="summarization", confidence=0.79, rationale="Vendor/agreement terms detected.")
        if any(token in lowered for token in ("agreement", "term", "termination", "liability", "indemnity", "confidential")):
            return ClassificationOutput(intent="contract", workflow="clause_extraction", confidence=0.82, rationale="Contract clause indicators detected.")
        return ClassificationOutput(intent="unknown", workflow="summarization", confidence=0.45, rationale="No strong domain indicators found.")

    def _summarize_text(self, text: str) -> tuple[str, str, str]:
        if self._llm is not None:
            try:
                summary, provider = self._llm.summarize(text)
                return summary, provider.name, provider.model
            except Exception as exc:  # pragma: no cover - external dependency behavior
                LOGGER.warning("LLM summarization failed across providers, using fallback summarizer: %s", exc)
        sentences = [chunk.strip() for chunk in re.split(r"[.!?]\s+", text) if chunk.strip()]
        if not sentences:
            return "No content available to summarize.", "rule-engine", "deterministic-v1"
        return " ".join(sentences[:3]), "rule-engine", "deterministic-v1"

    @staticmethod
    def _extract_clause_candidates(text: str) -> list[str]:
        numbered = re.findall(r"(?mi)^\s*\d+(?:\.\d+)*[\).\s-]+(.+)$", text)
        if numbered:
            return [match.strip() for match in numbered[:12]]
        keywords = ("termination", "liability", "indemnity", "confidentiality", "payment", "governing law", "warranty", "limitation of liability")
        candidates = [line.strip() for line in text.splitlines() if line.strip() and any(keyword in line.lower() for keyword in keywords)]
        if candidates:
            return candidates[:12]
        raise ClauseExtractionError("No contractual clauses matched expected patterns.")

    @staticmethod
    def _detect_risks(text: str) -> list[str]:
        risk_patterns = {
            "Missing ownership language": r"\b(ownership|ip rights|intellectual property)\b",
            "Unlimited liability exposure": r"\bunlimited liability\b",
            "Termination rights unclear": r"\btermination\b(?!.*(for convenience|for cause))",
            "Regulatory non-compliance signal": r"\b(non-compliance|violation|breach|penalty|fine)\b",
        }
        risks = [label for label, pattern in risk_patterns.items() if re.search(pattern, text, re.IGNORECASE)]
        return risks or ["No critical risk signals detected by rule engine."]

    @staticmethod
    def _audit(node: str, event: str, **details: Any) -> AuditEvent:
        return {"timestamp": datetime.now(timezone.utc).isoformat(), "node": node, "event": event, "details": details}
