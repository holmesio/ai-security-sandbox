"""Jailbreak / prompt-injection heuristics — STATUS: stub.

Start heuristic (regex + structural signals), measure precision/recall against a
labelled corpus, then decide whether a classifier or LLM-judge is worth the latency
and added injection surface (an LLM judge is itself injectable).

Signal ideas:
- Instruction-override phrases ("ignore previous", "disregard the above",
  "you are now", "developer mode").
- Role/format confusion ("### system", fake tool-call blocks, fake delimiters).
- Obfuscation: heavy leetspeak, char-by-char spacing, base64 that decodes to
  override phrases, translation-then-execute patterns.
- Ratio signals: unusually high imperative-verb density aimed at the assistant.

Output is a verdict + score + matched signals; the *caller* decides the policy
(block, flag-and-continue, require human review) based on context.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, Field


class JailbreakLabel(StrEnum):
    BENIGN = "benign"
    SUSPICIOUS = "suspicious"
    LIKELY_ATTACK = "likely_attack"


class JailbreakVerdict(BaseModel):
    label: JailbreakLabel
    score: float = Field(ge=0.0, le=1.0)
    signals: list[str] = Field(default_factory=list)


def detect_jailbreak(text: str) -> JailbreakVerdict:
    raise NotImplementedError("pair-program src/guardrails/jailbreak_detection.py")
