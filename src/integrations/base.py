"""LLM client wrapper — STATUS: stub.

Pairing notes:
- Constructor takes an explicit provider client + model id; no global singletons.
- `complete()` is the only public method. It: validates the request, applies the
  timeout, calls the provider, validates the response into `LLMResponse`, and
  returns it. Retries only on transient transport errors, capped (e.g. 2), with
  jittered backoff bounded by the overall deadline.
- No streaming in v1 (streaming complicates output validation — you can't validate
  a schema you haven't finished receiving).
"""

from __future__ import annotations

from src.integrations.schemas import LLMRequest, LLMResponse


class LLMClient:
    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise NotImplementedError("pair-program src/integrations/base.py")

    async def complete(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError
