from app.presentation.schemas.send_message_response_schema import (
    SendMessageResponseSchema,
)


def test_send_message_response_schema():
    schema = SendMessageResponseSchema(
        response="Assistant response.",
        current_state="clarification",
    )

    assert schema.response == "Assistant response."

    assert schema.current_state == "clarification"