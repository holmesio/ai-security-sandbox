"""Redis-backed abuse / DoS controls (OWASP LLM10: Unbounded Consumption).

Two complementary limiters, both enforced via atomic Redis Lua scripts:

- ``token_bucket``  — smooths request *rate* (requests/sec, burst).
- ``cost_based``    — caps cumulative *spend* (USD) per principal per rolling window.

Both fail **closed**: if Redis cannot be reached or the script errors, the call is
denied. See ``harness/PROJECT.md`` ADR-0002.
"""

from src.rate_limiters.cost_based import CostLimiter, CostDecision
from src.rate_limiters.token_bucket import TokenBucketLimiter, RateDecision

__all__ = [
    "CostLimiter",
    "CostDecision",
    "TokenBucketLimiter",
    "RateDecision",
]
