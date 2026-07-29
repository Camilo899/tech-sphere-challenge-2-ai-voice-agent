from app.domain.entities.conversation_context import ConversationContext
from app.domain.services.clinical_reasoner import ClinicalReasoner
from app.domain.value_objects.clinical_decision import ClinicalDecision
from app.domain.value_objects.conversation_state import ConversationState


def test_greeting_transitions_to_patient_verification():
    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    reasoner = ClinicalReasoner()

    updated_context = reasoner.next_step(context)

    assert (
        updated_context.current_state
        == ConversationState.PATIENT_VERIFICATION
    )