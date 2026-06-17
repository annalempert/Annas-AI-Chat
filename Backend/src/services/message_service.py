"""Business logic for persisting and retrieving chat messages."""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy.orm import Session

from src.utils.dal import MessageEntity


def _message_to_dict(message: MessageEntity) -> dict:
    """Convert a SQLAlchemy message entity into API-friendly camelCase JSON."""
    return {
        "id": message.id,
        "conversationId": message.conversation_id,
        "senderType": message.sender_type,
        "content": message.content,
        "createdAt": message.created_at,
    }


def create_message(db: Session, conversation_id: str, sender_type: str, content: str) -> dict:
    """Insert a new message for the given conversation."""
    message = MessageEntity(
        id=str(uuid4()),
        conversation_id=conversation_id,
        sender_type=sender_type,
        content=content,
        created_at=datetime.now(timezone.utc).replace(tzinfo=None),
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return _message_to_dict(message)


def list_messages_by_conversation(db: Session, conversation_id: str) -> list[dict]:
    """Return all messages for one conversation ordered oldest to newest."""
    messages = (
        db.query(MessageEntity)
        .filter(MessageEntity.conversation_id == conversation_id)
        .order_by(MessageEntity.created_at.asc())
        .all()
    )
    return [_message_to_dict(item) for item in messages]
