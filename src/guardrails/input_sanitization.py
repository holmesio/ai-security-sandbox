"""Input sanitization — STATUS: stub.

Runs first. Everything downstream assumes input has been through here.

Planned responsibilities:
- Unicode normalization (NFKC); strip / flag zero-width + bidi control chars used
  to smuggle instructions past detectors.
- Enforce byte and codepoint length ceilings (pre-flight token bomb defense, LLM10).
- Reject / flag disallowed encodings (base64 blobs, hex dumps) above a threshold.
- Never *rewrite* meaning — sanitization is normalization + rejection, not
  paraphrase. Return the cleaned text plus a list of applied transforms so the
  caller can log what changed.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class SanitizedInput(BaseModel):
    text: str
    original_len: int
    cleaned_len: int
    transforms: list[str] = Field(default_factory=list)
    flags: list[str] = Field(default_factory=list)  # e.g. "zero_width_stripped", "over_length"


def sanitize_input(raw: str, *, max_codepoints: int = 20_000) -> SanitizedInput:
    raise NotImplementedError("pair-program src/guardrails/input_sanitization.py")
