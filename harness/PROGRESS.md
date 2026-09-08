# PROGRESS — rolling build log

Newest entries on top. One row per meaningful change. `Secured?` = threat-model
abuse cases from `PROJECT.md §3` that this change actually mitigates (with a test
proving it), not just "should".

| Date | Component | Change | Tests | Secured? | Notes / follow-ups |
|------|-----------|--------|-------|----------|--------------------|
| 2026-09-08 | repo | Scaffolded `src/`, `harness/`, `docker/`, `tests/`; base compose (Redis + Qdrant); pyproject with dev deps | — | — | Next: pair-program cost-based rate limiter. |

## Component status board

| Component | State | Owner | Notes |
|-----------|-------|-------|-------|
| rate_limiters/cost_based | 🔴 not started | pair | **first pairing target** |
| rate_limiters/token_bucket | 🔴 not started | pair | shares Lua/Redis harness with cost_based |
| rag/vector_store | 🔴 not started | pair | filter-enforcement wrapper |
| rag/metadata_filter | 🔴 not started | pair | mandatory-filter model |
| rag/document_sanitization | 🔴 not started | pair | ADR-0004 |
| guardrails/input_sanitization | 🔴 not started | scaffold→pair | |
| guardrails/jailbreak_detection | 🔴 not started | pair | |
| guardrails/output_validation | 🔴 not started | pair | |
| integrations/base + schemas | 🔴 not started | scaffold→pair | |

Legend: 🔴 not started · 🟡 in progress · 🟢 built + tested · 🔵 red-teamed & hardened
