from datetime import UTC, datetime

from app.application.factories.conversation_orchestrator_factory import (
    create_conversation_orchestrator,
)
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


def test_orchestrator_processes_message():
    orchestrator = create_conversation_orchestrator()
    
    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    context.symptoms.append("fiebre")

    message = ConversationMessage(
        speaker="patient",
        content="Tengo fiebre desde ayer.",
        timestamp=datetime.now(UTC),
    )

    updated = orchestrator.process(
        context=context,
        message=message,
    )

    assert len(updated.messages) == 1

    assert updated.messages[0] is message

    assert (
        updated.clinical_decision
        is ClinicalDecision.ESCALATE
    )

    assert (
        updated.current_state
        is ConversationState.PATIENT_VERIFICATION
    )