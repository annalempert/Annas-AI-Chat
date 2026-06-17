"""Pydantic models for chat request and response payloads."""

from pydantic import BaseModel, Field

from src.models.message_model import MessageModel


class ChatRequestModel(BaseModel):
    """Incoming payload for POST /api/chat."""

    conversationId: str | None = None
    userMessage: str = Field(min_length=1)


class ChatResponseModel(BaseModel):
    """Successful chat response returned to the frontend."""

    conversationId: str
    assistantMessage: MessageModel
