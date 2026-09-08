# MEMORY — persistent knowledge store

Durable takeaways, edge cases, and OWASP notes. Not a changelog (that's
`PROGRESS.md`) and not a run log (that's `EVAL_LOG.md`). Add an entry when we learn
something that would be expensive to re-derive.

## OWASP Top 10 for LLM Applications (2025) — working reference

| ID | Name | How it shows up here | Where we defend |
|----|------|----------------------|-----------------|
| LLM01 | Prompt Injection (direct + indirect) | user override attempts; payloads inside retrieved docs | guardrails/jailbreak_detection, rag/document_sanitization |
| LLM02 | Sensitive Information Disclosure | secrets/PII in output or in retrieved chunks | guardrails/output_validation, rag/metadata_filter |
| LLM03 | Supply Chain | pinned model + client versions; SBOM of deps | integrations, pyproject pins |
| LLM04 | Data & Model Poisoning | poisoned docs at ingest surface later in retrieval | rag ingest sanitization + provenance metadata |
| LLM05 | Improper Output Handling | output rendered as HTML/SQL/shell downstream | guardrails/output_validation (schema + encode) |
| LLM06 | Excessive Agency | tool-calling with broad scope / no human gate | integrations (bounded tool set, no auto-exec) |
| LLM07 | System Prompt Leakage | model reveals system prompt on request | guardrails/output_validation, prompt design |
| LLM08 | Vector & Embedding Weaknesses | missing access filter; embedding inversion; cross-scope hits | rag/vector_store mandatory-filter wrapper |
| LLM09 | Misinformation | confident fabrication; over-reliance | integrations (cite-or-abstain), output validation |
| LLM10 | Unbounded Consumption | cost/DoS via floods, token bombs, recursive calls | rate_limiters/* (token-bucket + cost cap) |

## Design principles adopted

1. **Fail closed.** Any control that can't evaluate (Redis down, schema parse
   error, sanitizer exception) denies the request.
2. **Retrieved text is data, not instructions.** Always fenced + preamble; never
   raw-concatenated into the prompt (ADR-0004).
3. **Atomic or it didn't happen.** All check-and-consume on shared state is a single
   Redis Lua script — no `GET` then `SET`.
4. **Every reject has a machine-readable `reason` code** and a structured log line
   with `principal_id` + `request_id`.
5. **Filters are required arguments, not optional kwargs.** Make the unsafe call
   impossible to express, not just discouraged.
6. **Pre-flight before spend.** Estimate token cost locally (tiktoken) and reject
   oversized requests before any paid API call.

## Edge cases & gotchas discovered

_(none yet — fill as we build)_

- [ ] template: **<component>** — <what surprised us> — <why it matters> — <what we did>

## Open questions

- Cost model: charge on *estimated* pre-call tokens, reconcile with *actual* usage
  from the API response, or both (reserve then settle)? Leaning reserve-then-settle.
- Jailbreak detection: heuristic/regex only, a small classifier, or an LLM judge?
  Trade-off is latency + its own injection surface. Start heuristic, measure.
- RAG fence delimiter: random per-request nonce vs. fixed sentinel. Nonce resists
  ATK-010 but complicates prompt caching.
