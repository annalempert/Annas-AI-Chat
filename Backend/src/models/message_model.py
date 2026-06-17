"""Pydantic models representing chat messages."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class MessageModel(BaseModel):
    """Message object returned to API consumers."""

    id: str
    conversationId: str
    senderType: Literal["user", "assistant"]
    content: str
    createdAt: datetime


class CreateMessageModel(BaseModel):
    """Internal model for creating a message record."""

    conversationId: str
    senderType: Literal["user", "assistant"]
    content: str
