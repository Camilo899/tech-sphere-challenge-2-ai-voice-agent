from app.application.dtos.start_follow_up_response import (
    StartFollowUpResponse,
)


def test_start_follow_up_response():
    response = StartFollowUpResponse(
        conversation_id="conv-001",
        current_state="GREETING",
    )

    assert response.conversation_id == "conv-001"

    assert response.current_state == "GREETING"