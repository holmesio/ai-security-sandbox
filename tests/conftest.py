"""Shared fixtures.

- ``fake_redis``   — in-memory async Redis (``fakeredis``), incl. Lua eval, for unit
  tests of the rate limiters. No network.
- ``redis_client`` — real async client against the docker Redis; skipped unless
  ``-m integration`` and the service is reachable.
"""

from __future__ import annotations

import contextlib
from collections.abc import AsyncIterator

import pytest


@pytest.fixture
async def fake_redis() -> AsyncIterator[object]:
    fakeredis = pytest.importorskip("fakeredis")
    client = fakeredis.aioredis.FakeRedis(decode_responses=False)
    try:
        yield client
    finally:
        await client.aclose()


@pytest.fixture
async def redis_client() -> AsyncIterator[object]:
    redis_asyncio = pytest.importorskip("redis.asyncio")
    client = redis_asyncio.from_url("redis://localhost:6379/15")
    try:
        await client.ping()
    except Exception:  # noqa: BLE001
        pytest.skip("integration Redis not reachable on localhost:6379")
    try:
        await client.flushdb()
        yield client
    finally:
        with contextlib.suppress(Exception):
            await client.flushdb()
        await client.aclose()
