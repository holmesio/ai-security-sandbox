# AI Security Sandbox

A hands-on lab for building and breaking the security-critical layer that sits
between untrusted input and an LLM. Every module maps to one or more entries in
the [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/).

## Layout

| Path | Purpose | Primary OWASP LLM risks |
|------|---------|-------------------------|
| `src/guardrails/` | Input sanitization, jailbreak detection, output validation | LLM01, LLM05, LLM07 |
| `src/integrations/` | Secure LLM API wrappers with strict Pydantic I/O schemas | LLM05, LLM09, LLM03 |
| `src/rate_limiters/` | Redis-backed token-bucket + cost-based abuse/DoS control | LLM10 |
| `src/rag/` | Vector store access, metadata filtering, doc sanitization | LLM01 (indirect), LLM08, LLM02 |
| `harness/` | Project memory: scope, ADRs, threat model, progress, eval log | — |
| `docker/` | Local infra (Redis, Qdrant) via Docker Compose | — |
| `tests/` | pytest unit + integration + adversarial suites | — |

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env            # fill in ANTHROPIC_API_KEY
docker compose -f docker/docker-compose.yml up -d
pytest -m "not integration"
```

## Working agreement

Boilerplate is scaffolded; the security-critical core is pair-programmed.
The `harness/` markdown files are the source of truth for decisions and progress —
update them as we go.
