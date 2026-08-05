from app.presentation.schemas.start_follow_up_response_schema import (
    StartFollowUpResponseSchema,
)


def test_response_schema():
    schema = StartFollowUpResponseSchema(
        conversation_id="conv-001",
        current_state="GREETING",
    )

    assert schema.conversation_id == "conv-001"

    assert schema.current_state == "GREETING"