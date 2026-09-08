"""RAG pipeline: retrieval that assumes both the query and the corpus are hostile.

- ``metadata_filter``      — the mandatory access/scope filter model. Constructing a
  retrieval call without one is a type error, not a lint warning. (LLM08, LLM02)
- ``vector_store``         — thin wrapper over Qdrant that refuses to query without a
  filter and normalizes results into a typed shape. (LLM08)
- ``document_sanitization`` — clean chunk text of instruction-carrying patterns /
  control chars at *ingest* and again at *retrieval*, then fence it so the model
  treats it as data (ADR-0004). Defends indirect prompt injection. (LLM01, LLM04)
"""

from src.rag.document_sanitization import FencedContext, SanitizedChunk, sanitize_chunk
from src.rag.metadata_filter import AccessFilter
from src.rag.vector_store import RetrievedChunk, SecureVectorStore

__all__ = [
    "AccessFilter",
    "SecureVectorStore",
    "RetrievedChunk",
    "SanitizedChunk",
    "FencedContext",
    "sanitize_chunk",
]
