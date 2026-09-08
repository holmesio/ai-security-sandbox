"""Token-bucket rate limiter (request-rate smoothing).

STATUS: stub — to be pair-programmed.

Design intent (subject to change during pairing):
- One bucket per ``principal_id``; key = ``{namespace}:rl:tb:{principal_id}``.
- Redis Lua script does refill-and-consume atomically, storing ``(tokens, last_ts)``
  as a hash. No GET-then-SET from Python.
- Time source is Redis ``TIME`` (server clock) so multiple app processes agree.
- Key TTL set to a few refill periods so idle principals don't leak keys.
- Fails closed on ``redis.RedisError``.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RateDecision:
    allowed: bool
    reason: str  # machine-readable, e.g. "ok" | "rate_exceeded" | "backend_unavailable"
    tokens_remaining: float
    retry_after_s: float


class TokenBucketLimiter:
    """Placeholder. Real implementation lands during pairing."""

    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise NotImplementedError("pair-program src/rate_limiters/token_bucket.py")

    async def acquire(self, principal_id: str, cost: int = 1) -> RateDecision:
        raise NotImplementedError
