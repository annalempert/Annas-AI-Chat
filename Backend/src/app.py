"""FastAPI application entry point for the ChatGPT-like study API."""

from datetime import datetime, timezone
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.chat_controller import router as chat_router
from src.controllers.conversation_controller import router as conversation_router
from src.middleware.exception_handler import register_exception_handlers
from src.middleware.logger_middleware import LoggerMiddleware
from src.utils.app_config import get_config
from src.utils.dal import init_db

# Configure application-wide logging.
logging.basicConfig(level=logging.INFO)

# Create the FastAPI app instance.
app = FastAPI(title="ChatGPT-like Study API")
config = get_config()

# Allow the React frontend to call this API from a different origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Log every incoming request and its response time.
app.add_middleware(LoggerMiddleware)

# Convert unhandled exceptions into consistent JSON error responses.
register_exception_handlers(app)


@app.on_event("startup")
def startup_event():
    """Ensure database tables exist when the server starts."""
    init_db()


@app.get("/api/health")
def health_check():
    """Simple health endpoint used for monitoring and smoke tests."""
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}


# Register API route groups.
app.include_router(chat_router)
app.include_router(conversation_router)
