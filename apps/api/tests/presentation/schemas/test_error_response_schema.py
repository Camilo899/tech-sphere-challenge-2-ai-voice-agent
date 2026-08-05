from app.presentation.schemas.error_response_schema import (
    ErrorResponseSchema,
)


def test_error_response_schema():
    schema = ErrorResponseSchema(
        error="Internal Server Error",
        detail="Unexpected error",
    )

    assert schema.error == "Internal Server Error"

    assert schema.detail == "Unexpected error"