"""Secure Qdrant wrapper — STATUS: stub.

Enforces ADR-0003: no query without an `AccessFilter`. The filter is a required
positional argument on every retrieval method; there is no default and no kwarg
form that omits it.

Pairing notes:
- `search()` signature: `search(self, query_vector, access: AccessFilter, *, limit)`.
- The `AccessFilter.to_qdrant()` output is always ANDed into the Qdrant query —
  callers cannot pass their own raw filter that might replace it.
- Results normalized to `RetrievedChunk` (text + metadata + score + provenance);
  raw Qdrant points never escape this module.
- On any client error: raise. No silent empty-list (an empty list looks like "no
  results" and could mask a broken filter).
"""

from __future__ import annotations

from collections.abc import Sequence

from pydantic import BaseModel, Field

from src.rag.metadata_filter import AccessFilter


class RetrievedChunk(BaseModel):
    chunk_id: str
    text: str
    score: float
    scope: str
    provenance: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)


class SecureVectorStore:
    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise NotImplementedError("pair-program src/rag/vector_store.py")

    async def search(
        self,
        query_vector: Sequence[float],
        access: AccessFilter,
        *,
        limit: int = 5,
    ) -> list[RetrievedChunk]:
        raise NotImplementedError
