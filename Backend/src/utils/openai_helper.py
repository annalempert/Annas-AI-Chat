"""Helper module for calling the OpenAI Chat Completions API from the backend only."""

from fastapi import HTTPException
from openai import OpenAI

from src.utils.app_config import get_config


def generate_assistant_response(history: list[dict]) -> str:
    """
    Send the full conversation history to OpenAI and return the assistant reply.

    The OpenAI API key is read from environment variables and never exposed to the frontend.
    """
    config = get_config()
    if not config.openai_api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key is missing")

    client = OpenAI(api_key=config.openai_api_key)

    # Convert stored messages into the role/content format expected by OpenAI.
    messages = [{"role": item["senderType"], "content": item["content"]} for item in history]

    try:
        completion = client.chat.completions.create(model=config.openai_model, messages=messages)
        return completion.choices[0].message.content or ""
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"OpenAI request failed: {exc}") from exc
