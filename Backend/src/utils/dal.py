"""Database access layer: SQLAlchemy engine, ORM entities, and session helpers."""

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, sessionmaker

from src.utils.app_config import get_config

# Base class for all SQLAlchemy ORM models.
Base = declarative_base()


class ConversationEntity(Base):
    """ORM mapping for the conversations table."""

    __tablename__ = "conversations"

    id = Column(String(36), primary_key=True)
    title = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=False), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=False), nullable=False, default=lambda: datetime.now(timezone.utc))
    messages = relationship("MessageEntity", back_populates="conversation", cascade="all, delete-orphan")


class MessageEntity(Base):
    """ORM mapping for the messages table."""

    __tablename__ = "messages"

    id = Column(String(36), primary_key=True)
    conversation_id = Column(String(36), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    sender_type = Column(Enum("user", "assistant", name="sender_type"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=False), nullable=False, default=lambda: datetime.now(timezone.utc))

    conversation = relationship("ConversationEntity", back_populates="messages")


def get_engine():
    """Create a SQLAlchemy engine using the configured database URL."""
    config = get_config()
    return create_engine(config.database_url, pool_pre_ping=True)


# Shared engine and session factory used by the application.
engine = get_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db() -> None:
    """Create database tables if they do not already exist."""
    Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    """FastAPI dependency that yields a database session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
