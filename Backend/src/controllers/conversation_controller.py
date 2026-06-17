"""HTTP routes for conversation CRUD operations."""

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.services.conversation_service import create_conversation, delete_conversation, list_conversations
from src.services.message_service import list_messages_by_conversation
from src.utils.dal import get_db

router = APIRouter(prefix="/api/conversations", tags=["conversations"])


@router.post("")
def create_conversation_route(db: Session = Depends(get_db)):
    """Create a new empty conversation."""
    data = create_conversation(db)
    return {"success": True, "data": data}


@router.get("")
def list_conversations_route(db: Session = Depends(get_db)):
    """Return all conversations ordered by most recently updated."""
    data = list_conversations(db)
    return {"success": True, "data": data}


@router.get("/{conversation_id}/messages")
def get_messages_route(conversation_id: str, db: Session = Depends(get_db)):
    """Return all messages for a specific conversation in chronological order."""
    data = list_messages_by_conversation(db, conversation_id)
    return {"success": True, "data": data}


@router.delete("/{conversation_id}", status_code=204)
def delete_conversation_route(conversation_id: str, db: Session = Depends(get_db)):
    """Delete a conversation and cascade-delete its messages."""
    delete_conversation(db, conversation_id)
    return Response(status_code=204)
