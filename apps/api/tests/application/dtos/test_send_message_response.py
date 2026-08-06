from app.application.dtos.send_message_response import (
    SendMessageResponse,
)


def test_send_message_response():
    response = SendMessageResponse(
        response="Thank you for the update.",
        current_state="symptom_collection",
    )

    assert response.response == "Thank you for the update."

    assert response.current_state == "symptom_collection"