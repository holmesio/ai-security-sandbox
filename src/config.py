"""Central settings, loaded from environment / .env.

Kept deliberately small: only cross-cutting config lives here. Component-specific
policy (bucket sizes, sanitizer rule sets) belongs with the component so it can be
versioned and reasoned about in isolation.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # --- LLM ---
    anthropic_api_key: str = Field(default="", repr=False)
    llm_default_model: str = "claude-sonnet-5"
    llm_request_timeout_s: float = 30.0

    # --- Redis ---
    redis_url: str = "redis://localhost:6379/0"
    redis_namespace: str = "aiss"

    # --- Qdrant ---
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str = Field(default="", repr=False)
    qdrant_collection: str = "aiss_docs"

    # --- Budget / abuse controls ---
    cost_limit_usd_per_hour: float = 2.00
    cost_limit_usd_per_day: float = 20.00
    max_input_tokens_per_request: int = 12_000


settings = Settings()
