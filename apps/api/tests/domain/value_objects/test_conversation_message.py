from datetime import UTC, datetime

from app.domain.value_objects.conversation_message import (
    ConversationMessage,
)


def test_conversation_message_creation():
    timestamp = datetime.now(UTC)

    message = ConversationMessage(
        speaker="patient",
        content="Tengo dolor en la herida.",
        timestamp=timestamp,
    )

    assert message.speaker == "patient"
    assert message.content == "Tengo dolor en la herida."
    assert message.timestamp == timestamp