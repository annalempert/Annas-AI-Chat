"""Pydantic model representing a conversation resource."""

from datetime import datetime

from pydantic import BaseModel


class ConversationModel(BaseModel):
    """Shape of a conversation returned by the API."""

    id: str
    title: str
    createdAt: datetime
    updatedAt: datetime
