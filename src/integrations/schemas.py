"""Strict I/O schemas for the LLM boundary — STATUS: stub (shape is illustrative).

These are the contract. `model_config` uses `extra="forbid"` everywhere so an
unexpected field from either the caller or the provider is a hard error, not a
silent passthrough.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Role(StrEnum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")
    role: Role
    content: str = Field(min_length=1, max_length=200_000)


class LLMRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    model: str
    messages: list[Message] = Field(min_length=1)
    max_output_tokens: int = Field(gt=0, le=8192)
    temperature: float = Field(ge=0.0, le=1.0, default=0.2)
    # Principal on whose budget this call is charged; flows to the cost limiter.
    principal_id: str = Field(min_length=1)


class TokenUsage(BaseModel):
    model_config = ConfigDict(extra="forbid")
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)


class LLMResponse(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    model: str
    text: str
    usage: TokenUsage
    stop_reason: str
