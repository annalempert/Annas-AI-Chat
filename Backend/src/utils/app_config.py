"""Load and expose application configuration from environment variables."""

import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel

# Read values from Backend/.env into the process environment.
load_dotenv()


class AppConfig(BaseModel):
    """Typed configuration object used across the backend."""

    database_url: str
    openai_api_key: str
    openai_model: str
    cors_origins: list[str]
    app_host: str
    app_port: int


@lru_cache
def get_config() -> AppConfig:
    """Return a cached AppConfig instance built from environment variables."""
    origins = os.getenv("CORS_ORIGINS", "http://localhost:5173")
    return AppConfig(
        database_url=os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/chat_app"),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        cors_origins=[origin.strip() for origin in origins.split(",") if origin.strip()],
        app_host=os.getenv("APP_HOST", "0.0.0.0"),
        app_port=int(os.getenv("APP_PORT", "8000")),
    )
