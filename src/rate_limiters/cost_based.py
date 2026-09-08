"""Cost-based limiter — caps cumulative USD spend per principal per rolling window.

STATUS: stub — **first pairing target**.

Why this exists (OWASP LLM10): request-rate limiting alone doesn't stop a well-paced
attacker from running up a large bill, nor a single legitimate-looking request with
a huge context window. This limiter tracks *money*, not requests.

Open design questions to settle while pairing (see harness/MEMORY.md):
- Accounting model: reserve-then-settle (estimate tokens pre-call, reserve the
  estimated cost, then reconcile against the provider's reported usage) vs.
  charge-on-estimate vs. charge-on-actual-only.
- Window shape: fixed calendar bucket, sliding log, or sliding-window-counter.
  Sliding-window-counter is cheap in Redis and good enough; a burst attacker
  can't hide in bucket-boundary effects.
- Concurrency: N requests from one principal arriving together must not each see
  "budget available" and collectively blow the cap (ATK-003 / TOCTOU). The
  reserve step is the atomic Lua op.
- Fail-closed on Redis error, and decide: does an in-flight reservation that never
  gets settled (app crash) expire on its own? (Reservation keys need a TTL.)

Sketch of the interface only:
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class CostDecision:
    allowed: bool
    reason: str  # "ok" | "hourly_cap" | "daily_cap" | "request_too_large" | "backend_unavailable"
    reservation_id: str | None
    spent_usd_window: Decimal
    limit_usd_window: Decimal
    retry_after_s: float


class CostLimiter:
    """Placeholder. Real implementation + Lua script land during pairing."""

    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise NotImplementedError("pair-program src/rate_limiters/cost_based.py")

    async def reserve(self, principal_id: str, estimated_usd: Decimal) -> CostDecision:
        """Atomically check every active window and reserve ``estimated_usd``."""
        raise NotImplementedError

    async def settle(self, reservation_id: str, actual_usd: Decimal) -> None:
        """Reconcile a reservation against real usage from the provider response."""
        raise NotImplementedError

    async def release(self, reservation_id: str) -> None:
        """Return a reservation to the pool (call failed before spend)."""
        raise NotImplementedError
