"""Mandatory retrieval access filter — STATUS: stub.

The whole point: you cannot call the vector store without one of these. It encodes
*who is asking* and *what scope they may see*, and compiles to a Qdrant payload
filter server-side (never filtered client-side after an unfiltered fetch).

Pairing notes:
- Model should be constructed from a request principal/tenant/ACL context, not from
  free-form kwargs.
- `.to_qdrant()` produces the `qdrant_client.models.Filter`. Deny-by-default:
  empty/None scope compiles to a filter that matches nothing, not everything.
- Consider a `require_provenance` flag that also filters out chunks whose ingest
  provenance is missing/untrusted (LLM04).
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class AccessFilter(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    principal_id: str = Field(min_length=1)
    tenant_id: str = Field(min_length=1)
    # Collections / namespaces this principal is entitled to read.
    allowed_scopes: frozenset[str] = Field(min_length=1)
    require_trusted_provenance: bool = True

    def to_qdrant(self) -> object:
        """Compile to a qdrant_client.models.Filter. Deny-by-default."""
        raise NotImplementedError("pair-program src/rag/metadata_filter.py")
