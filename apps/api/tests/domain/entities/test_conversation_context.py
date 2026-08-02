from datetime import UTC, datetime

from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.conversation_message import (
    ConversationMessage,
)
from app.domain.value_objects.conversation_state import (
    ConversationState,
)


def test_add_message_to_conversation():
    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    message = ConversationMessage(
        speaker="patient",
        content="Tengo fiebre.",
        timestamp=datetime.now(UTC),
    )

    context.add_message(message)

    assert len(context.messages) == 1

    assert context.messages[0] is message