"""Business logic for the main chat flow: save messages, call OpenAI, return reply."""

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from src.services.conversation_service import create_conversation, get_conversation_or_404
from src.services.message_service import create_message, list_messages_by_conversation
from src.utils.openai_helper import generate_assistant_response


def _message_preview(content: str) -> str:
    """Create a short conversation title from the first user message."""
    content = content.strip()
    return content[:50] if len(content) > 50 else content


def send_chat_message(db: Session, conversation_id: str | None, user_message: str) -> dict:
    """
    Orchestrate the full chat workflow:
    1. Create or load a conversation
    2. Save the user message
    3. Send full history to OpenAI
    4. Save and return the assistant message
    """
    if not user_message.strip():
        raise ValueError("userMessage must not be empty")

    # Continue an existing conversation or create a new one.
    if conversation_id:
        conversation = get_conversation_or_404(db, conversation_id)
    else:
        conversation_payload = create_conversation(db, title=_message_preview(user_message) or "New Chat")
        conversation = get_conversation_or_404(db, conversation_payload["id"])

    # Persist the user message before requesting the assistant response.
    create_message(db, conversation.id, "user", user_message)
    history = list_messages_by_conversation(db, conversation.id)
    assistant_text = generate_assistant_response(history)
    assistant_message = create_message(db, conversation.id, "assistant", assistant_text)

    # Update conversation metadata after a successful exchange.
    conversation.updated_at = datetime.now(timezone.utc).replace(tzinfo=None)
    if conversation.title == "New Chat":
        conversation.title = _message_preview(user_message) or "New Chat"
    db.add(conversation)
    db.commit()

    return {"conversationId": conversation.id, "assistantMessage": assistant_message}
