"""Centralized exception handlers that return a consistent JSON error envelope."""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI) -> None:
    """Register global HTTP and generic exception handlers on the FastAPI app."""

    @app.exception_handler(HTTPException)
    async def http_exception_handler(_: Request, exc: HTTPException):
        """Convert raised HTTPException instances into JSON error responses."""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {"code": "HTTP_ERROR", "message": exc.detail},
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(_: Request, exc: Exception):
        """Catch unexpected errors and return a safe 500 response."""
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {"code": "INTERNAL_SERVER_ERROR", "message": str(exc)},
            },
        )
