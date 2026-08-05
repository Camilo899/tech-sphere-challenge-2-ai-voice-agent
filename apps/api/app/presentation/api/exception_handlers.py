from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.presentation.schemas.error_response_schema import (
    ErrorResponseSchema,
)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Registers global exception handlers.
    """

    @app.exception_handler(Exception)
    async def unexpected_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        response = ErrorResponseSchema(
            error="Internal Server Error",
            detail=str(exc),
        )

        return JSONResponse(
            status_code=500,
            content=response.model_dump(),
        )