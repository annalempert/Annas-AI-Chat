"""Business logic for creating, listing, updating, and deleting conversations."""

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.utils.dal import ConversationEntity


def _conversation_to_dict(conversation: ConversationEntity) -> dict:
    """Convert a SQLAlchemy conversation entity into API-friendly camelCase JSON."""
    return {
        "id": conversation.id,
        "title": conversation.title,
        "createdAt": conversation.created_at,
        "updatedAt": conversation.updated_at,
    }


def create_conversation(db: Session, title: str = "New Chat") -> dict:
    """Insert a new conversation row and return its serialized representation."""
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    conversation = ConversationEntity(id=str(uuid4()), title=title, created_at=now, updated_at=now)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return _conversation_to_dict(conversation)


def list_conversations(db: Session) -> list[dict]:
    """Return conversations sorted by latest activity."""
    conversations = db.query(ConversationEntity).order_by(ConversationEntity.updated_at.desc()).all()
    return [_conversation_to_dict(item) for item in conversations]


def get_conversation_or_404(db: Session, conversation_id: str) -> ConversationEntity:
    """Load a conversation by ID or raise HTTP 404 if it does not exist."""
    conversation = db.query(ConversationEntity).filter(ConversationEntity.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation


def touch_conversation(db: Session, conversation_id: str) -> None:
    """Update only the conversation updated_at timestamp."""
    conversation = get_conversation_or_404(db, conversation_id)
    conversation.updated_at = datetime.now(timezone.utc).replace(tzinfo=None)
    db.commit()


def delete_conversation(db: Session, conversation_id: str) -> None:
    """Delete a conversation; related messages are removed by FK cascade."""
    conversation = get_conversation_or_404(db, conversation_id)
    db.delete(conversation)
    db.commit()
