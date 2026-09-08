"""Guardrails: what goes into the model and what comes out.

- ``input_sanitization``  — normalize + bound untrusted input (unicode, control
  chars, length, encoding tricks) before any detection runs. (LLM01, LLM10)
- ``jailbreak_detection`` — heuristic detection of instruction-override / role-play
  / obfuscation attempts. (LLM01)
- ``output_validation``   — structural + policy validation of model output:
  schema conformance, secret/system-prompt leak checks, active-markup neutralization
  for downstream renderers. (LLM05, LLM07, LLM02)

All three fail closed: a sanitizer/validator exception => request denied.
"""

from src.guardrails.input_sanitization import SanitizedInput, sanitize_input
from src.guardrails.jailbreak_detection import JailbreakVerdict, detect_jailbreak
from src.guardrails.output_validation import OutputVerdict, validate_output

__all__ = [
    "SanitizedInput",
    "sanitize_input",
    "JailbreakVerdict",
    "detect_jailbreak",
    "OutputVerdict",
    "validate_output",
]
