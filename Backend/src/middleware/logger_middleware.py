"""Middleware that logs each HTTP request method, path, status code, and duration."""

import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("chat-app")


class LoggerMiddleware(BaseHTTPMiddleware):
    """Log basic request/response information for observability."""

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000

        logger.info(
            "%s %s -> %s in %.2fms",
            request.method,
            request.url.path,
            response.status_code,
            process_time,
        )
        return response
