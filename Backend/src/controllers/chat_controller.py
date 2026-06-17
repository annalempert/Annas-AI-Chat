"""HTTP routes for the chat endpoint. Controllers only map requests to services."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.chat_model import ChatRequestModel
from src.services.chat_service import send_chat_message
from src.utils.dal import get_db

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("")
def chat_route(payload: ChatRequestModel, db: Session = Depends(get_db)):
    """
    Receive a user message, optionally continue an existing conversation,
    and return the assistant response from the backend service layer.
    """
    try:
        data = send_chat_message(db, payload.conversationId, payload.userMessage)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"success": True, "data": data}
