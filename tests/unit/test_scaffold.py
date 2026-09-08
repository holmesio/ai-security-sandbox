"""Smoke test: the package tree imports cleanly and stubs advertise themselves.

Replaced component-by-component as real implementations land.
"""

import importlib

import pytest

MODULES = [
    "src.config",
    "src.guardrails",
    "src.integrations",
    "src.rate_limiters",
    "src.rag",
]


@pytest.mark.parametrize("mod", MODULES)
def test_imports(mod: str) -> None:
    importlib.import_module(mod)


def test_cost_limiter_is_still_a_stub() -> None:
    from src.rate_limiters.cost_based import CostLimiter

    with pytest.raises(NotImplementedError):
        CostLimiter()
