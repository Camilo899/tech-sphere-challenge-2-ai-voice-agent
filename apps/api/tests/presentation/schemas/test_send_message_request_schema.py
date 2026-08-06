from app.presentation.schemas.send_message_request_schema import (
    SendMessageRequestSchema,
)


def test_send_message_request_schema():
    schema = SendMessageRequestSchema(
        conversation_id="conv-001",
        message="Patient message.",
    )

    assert schema.conversation_id == "conv-001"

    assert schema.message == "Patient message."