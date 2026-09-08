"""Output validation — STATUS: stub.

The model's output is untrusted. Before it reaches a caller or a downstream
renderer/executor:

- **Schema:** if a structured response was requested, it must parse into the
  declared Pydantic model or the whole response is rejected (no "best effort").
- **Leak checks:** scan for system-prompt fragments (LLM07) and secret patterns
  (API keys, tokens, PII shapes) (LLM02).
- **Active markup:** for text destined to be rendered, neutralize/encode HTML/JS,
  markdown links to `javascript:`, and SQL-ish payloads (LLM05). Encoding is the
  caller's responsibility per sink; we flag + optionally strip.
- **Refusal/abstain honoring:** if the integration layer asked for "cite or
  abstain", an answer with no citations is downgraded (LLM09).
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class OutputVerdict(BaseModel):
    allowed: bool
    reason: str  # "ok" | "schema_violation" | "secret_leak" | "system_prompt_leak" | "active_markup" | "uncited"
    findings: list[str] = Field(default_factory=list)
    safe_text: str | None = None  # populated when we produced a neutralized version


def validate_output(text: str, *, expect_schema: type[BaseModel] | None = None) -> OutputVerdict:
    raise NotImplementedError("pair-program src/guardrails/output_validation.py")
