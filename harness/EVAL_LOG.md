# EVAL_LOG — adversarial test runs

Tracks red-team scripts and their results. Every attack we simulate gets an ID,
lives as a test under `tests/` (marked `@pytest.mark.adversarial`), and is logged
here with outcome. A run is only "passed" if the defense **blocked or contained**
the attack *and* emitted the expected log/`reason` code.

## Attack catalogue

| ID | Attack | Target layer | OWASP | Test | Status |
|----|--------|--------------|-------|------|--------|
| ATK-001 | Budget exhaustion via request flood | rate_limiters/cost_based | LLM10 | _tbd_ | ⬜ not written |
| ATK-002 | Token-flood: one request with oversized context | guardrails + rate_limiters | LLM10 | _tbd_ | ⬜ not written |
| ATK-003 | Concurrent burst races the cost check (TOCTOU) | rate_limiters/cost_based | LLM10 | _tbd_ | ⬜ not written |
| ATK-004 | Redis unreachable → limiter bypass attempt | rate_limiters | LLM10 | _tbd_ | ⬜ not written |
| ATK-005 | Direct jailbreak / instruction override | guardrails/jailbreak_detection | LLM01 | _tbd_ | ⬜ not written |
| ATK-006 | Indirect injection in a retrieved document | rag/document_sanitization | LLM01, LLM04 | _tbd_ | ⬜ not written |
| ATK-007 | Retrieval without metadata filter (cross-scope read) | rag/vector_store | LLM08, LLM02 | _tbd_ | ⬜ not written |
| ATK-008 | System-prompt / secret exfiltration in output | guardrails/output_validation | LLM07, LLM02 | _tbd_ | ⬜ not written |
| ATK-009 | Output contains active markup (HTML/JS/SQL) | guardrails/output_validation | LLM05 | _tbd_ | ⬜ not written |
| ATK-010 | Delimiter-injection: doc contains the fence delimiter | rag/document_sanitization | LLM01 | _tbd_ | ⬜ not written |

Status: ⬜ not written · 🟠 written, failing (defense gap) · ✅ passing · ♻️ regression-guarded

## Run log

Newest on top.

### <date> — <ATK-id> — <short title>
- **Commit:** `<sha>`
- **Command:** `pytest tests/... -m adversarial -k ...`
- **Result:** pass / fail
- **Observed:** what the defense did (reject reason code, log lines, containment)
- **Gap / fix:** what changed as a result
- **Follow-up:** new attack ideas this surfaced

---

_First real entry lands when we finish the cost-based rate limiter and write ATK-001/003/004._
