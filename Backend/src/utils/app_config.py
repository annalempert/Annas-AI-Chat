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


def _resolve_database_url() -> str:
    """Build the DB URL for Docker from Backend/.env, or use DATABASE_URL locally."""
    default = "mysql+pymysql://root:password@localhost:3306/chat_app"
    mysql_host = os.getenv("MYSQL_HOST")
    if not mysql_host:
        return os.getenv("DATABASE_URL", default)

    password = os.getenv("MYSQL_ROOT_PASSWORD", "")
    database = os.getenv("MYSQL_DATABASE", "chat_app")
    port = os.getenv("MYSQL_PORT", "3306")
    return f"mysql+pymysql://root:{password}@{mysql_host}:{port}/{database}"


@lru_cache
def get_config() -> AppConfig:
    """Return a cached AppConfig instance built from environment variables."""
    origins = os.getenv("CORS_ORIGINS", "http://localhost:5173")
    return AppConfig(
        database_url=_resolve_database_url(),
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        cors_origins=[origin.strip() for origin in origins.split(",") if origin.strip()],
        app_host=os.getenv("APP_HOST", "0.0.0.0"),
        app_port=int(os.getenv("APP_PORT", "8000")),
    )
