from __future__ import annotations

from dataclasses import dataclass
from operator import add
from typing import Annotated, Any, Literal

from typing_extensions import TypedDict

from pydantic import BaseModel, Field


class AuditEvent(TypedDict):
    timestamp: str
    node: str
    event: str
    details: dict[str, Any]


class PipelineState(TypedDict):
    document_id: str
    document_text: str
    intent: str
    confidence: float
    selected_workflow: str
    status: str
    summary: str
    clauses: list[str]
    risks: list[str]
    llm_provider: str
    llm_model: str
    extraction_attempts: int
    max_extraction_attempts: int
    clause_extraction_succeeded: bool
    errors: Annotated[list[str], add]
    route_history: Annotated[list[str], add]
    audit_log: Annotated[list[AuditEvent], add]


class ClassificationOutput(BaseModel):
    intent: Literal["contract", "compliance_report", "vendor_agreement", "unknown"]
    workflow: Literal["summarization", "clause_extraction", "risk_detection"]
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


@dataclass
class ProviderRuntime:
    name: Literal["gemini", "groq", "huggingface"]
    model: str
    max_output_tokens: int
    client: Any


@dataclass
class ProviderHealth:
    consecutive_failures: int = 0
    unavailable_until: float = 0.0
