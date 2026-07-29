from app.domain.entities.conversation_context import ConversationContext
from app.domain.value_objects.clinical_decision import ClinicalDecision
from app.domain.value_objects.conversation_state import ConversationState


def test_conversation_context_creation():
    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    assert context.conversation_id == "conv-001"
    assert context.current_state == ConversationState.GREETING
    assert context.clinical_decision == ClinicalDecision.CONTINUE

    assert context.symptoms == []
    assert context.evidences == []
    assert context.messages == []