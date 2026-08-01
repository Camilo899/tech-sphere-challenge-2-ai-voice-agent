from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.conversation_orchestrator import (
    ConversationOrchestrator,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.conversation_state import (
    ConversationState,
)


def test_orchestrator_updates_context():
    orchestrator = ConversationOrchestrator()

    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    context.symptoms.append("fiebre")

    updated = orchestrator.process(context)

    assert updated.clinical_decision is ClinicalDecision.ESCALATE

    assert (
        updated.current_state
        is ConversationState.PATIENT_VERIFICATION
    )