# PROJECT — AI Security Sandbox

## 1. Scope

Build the defensive middleware layer between untrusted input and an LLM, then
red-team it. Deliverables, in priority order:

1. **Cost-based rate limiter** — Redis-backed, atomic, principal-scoped spend caps
   (LLM10 Unbounded Consumption).
2. **Secure RAG pipeline** — retrieval with mandatory metadata filtering + document
   sanitization against indirect prompt injection (LLM01 indirect, LLM08).
3. **Guardrails** — input sanitization, jailbreak/heuristic detection, structured
   output validation (LLM01, LLM05, LLM07).
4. **Secure LLM integration wrapper** — strict Pydantic request/response schemas,
   timeouts, retries, no unbounded fan-out (LLM05, LLM09).

**Out of scope:** model training/fine-tuning, hosting inference, production IAM,
multi-tenant billing. This is a learning sandbox; infra is laptop-grade.

## 2. Architecture overview

```
                 ┌─────────────┐
  caller ──req──▶ │  Guardrails │ input sanitization + jailbreak detection
                 └──────┬──────┘
                        ▼
                 ┌─────────────┐   pre-flight token estimate
                 │ RateLimiter │   token-bucket (rps) + cost cap (USD/window)
                 └──────┬──────┘   atomic check-and-consume in Redis (Lua)
                        ▼
                 ┌─────────────┐
                 │     RAG      │  metadata filter (mandatory) → retrieve →
                 └──────┬──────┘  sanitize docs → wrap in untrusted-content fence
                        ▼
                 ┌─────────────┐
                 │ Integration │  Pydantic-validated request → LLM → Pydantic
                 └──────┬──────┘  -validated response; timeout + bounded retry
                        ▼
                 ┌─────────────┐
                 │  Guardrails │  output validation / schema + policy checks
                 └──────┬──────┘
                        ▼
                     caller
```

Cross-cutting: structured logging with a `principal_id` + `request_id` on every
hop; every reject is logged with a machine-readable `reason` code.

## 3. Threat model notes

**Trust boundaries**
- End-user input: fully untrusted (prompt injection, oversized payloads, unicode
  abuse, token flooding).
- Retrieved documents: **untrusted** even if from "our" store — they may have been
  poisoned at ingest (LLM04) or authored to carry injection payloads (LLM01
  indirect). Treat retrieved text as data, never as instructions.
- LLM output: untrusted — may contain injected instructions, leaked system prompt
  (LLM07), fabricated facts (LLM09), or unsafe markup/HTML/SQL (LLM05).
- Redis: trusted infra, but availability-sensitive — if it's down the limiter must
  **fail closed** (deny), not fail open.

**Key abuse cases we defend against**
| # | Abuse case | Layer | OWASP |
|---|------------|-------|-------|
| A1 | Attacker loops cheap requests to exhaust budget / rack up cost | RateLimiter (cost) | LLM10 |
| A2 | Single huge-context request (token flooding) | Guardrails pre-flight + RateLimiter | LLM10 |
| A3 | Direct jailbreak ("ignore previous instructions…") | Guardrails (jailbreak detection) | LLM01 |
| A4 | Poisoned/injection-laden document surfaces in retrieval | RAG (sanitization + fencing) | LLM01, LLM04 |
| A5 | Cross-tenant/authz retrieval by omitting a filter | RAG (mandatory metadata filter) | LLM08, LLM02 |
| A6 | Model emits system prompt / secrets | Guardrails (output validation) | LLM07, LLM02 |
| A7 | Model output rendered as HTML/markdown → XSS downstream | Guardrails (output validation) | LLM05 |
| A8 | Redis outage used to bypass limits | RateLimiter (fail-closed) | LLM10 |

**Explicit non-goals of the threat model:** nation-state persistence, supply-chain
compromise of the base model, side-channel timing attacks on embeddings.

## 4. Architecture Decision Records (ADRs)

ADRs are append-only. Supersede, don't edit. Status: Proposed | Accepted | Superseded.

---

### ADR-0001 — Language & runtime stack
**Status:** Accepted · 2026-09-08
**Context:** Need fast iteration, strong typing at I/O boundaries, good async story
for concurrent LLM calls and Redis.
**Decision:** Python 3.12+, `async`-first, Pydantic v2 for every trust-boundary
schema, `redis.asyncio`, `qdrant-client`, `httpx`. Lint `ruff`, types `mypy --strict`.
**Consequences:** Pydantic validation cost on hot path (acceptable). Async means we
must be disciplined about shared state and cancellation.

---

### ADR-0002 — Redis as the rate-limiter state store
**Status:** Accepted · 2026-09-08
**Context:** Rate/cost limiting needs shared, low-latency, atomic counters across
processes.
**Decision:** Redis with **server-side Lua scripts** for all check-and-consume
operations so the read-modify-write is atomic (no TOCTOU between `GET` and `SET`).
`maxmemory-policy noeviction` so limiter keys are never silently evicted.
**Consequences:** Lua logic must be tested against `fakeredis`. Redis becomes a hard
dependency on the request path → limiter **fails closed** on connection error.
**Alternatives rejected:** in-process counters (not shared), `INCR`+`EXPIRE` without
Lua (race between the two commands), a dedicated quota service (overkill here).

---

### ADR-0003 — Qdrant as the vector store
**Status:** Accepted · 2026-09-08
**Context:** Need payload/metadata filtering that is enforced *server-side* at query
time, plus a local Docker image.
**Decision:** Qdrant. RAG layer wraps the client so that **no query can be issued
without an explicit metadata filter object** (filter is a required constructor arg,
not an optional kwarg).
**Consequences:** Slightly more ceremony per query. Swapping to Chroma later means
re-implementing the filter-enforcement wrapper.

---

### ADR-0004 — Retrieved content is fenced, never concatenated raw
**Status:** Proposed · 2026-09-08
**Context:** Indirect prompt injection (A4) rides in on retrieved document text.
**Decision:** Sanitized document chunks are wrapped in an explicit, non-forgeable
delimiter block and prefixed with a data-not-instructions preamble before being
placed in the prompt. Sanitization strips/escapes known instruction-carrying
patterns and control characters. Details TBD during pairing on the RAG pipeline.
**Consequences:** Prompt token overhead per chunk. Delimiter choice must resist the
document containing the delimiter itself.

---

_Add new ADRs above this line as `ADR-000N`._
