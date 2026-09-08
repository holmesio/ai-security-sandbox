"""Secure LLM API wrappers.

Goal: make the *unsafe* call hard to express. The wrapper:
- Takes a validated ``LLMRequest`` (Pydantic) and returns a validated
  ``LLMResponse``; malformed provider output raises, never leaks through.
- Enforces a hard timeout and a *bounded* retry policy (no unbounded backoff loop
  that itself becomes a cost sink — LLM10).
- Pins model + client version (LLM03) and records token usage for the cost limiter
  to settle against.
- Exposes no raw ``**kwargs`` passthrough to the provider SDK.
"""

from src.integrations.base import LLMClient
from src.integrations.schemas import LLMRequest, LLMResponse, TokenUsage

__all__ = ["LLMClient", "LLMRequest", "LLMResponse", "TokenUsage"]
