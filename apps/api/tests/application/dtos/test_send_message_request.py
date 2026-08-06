from app.application.dtos.send_message_request import (
    SendMessageRequest,
)


def test_send_message_request():
    request = SendMessageRequest(
        conversation_id="conv-001",
        message="I feel much better today.",
    )

    assert request.conversation_id == "conv-001"

    assert request.message == "I feel much better today."