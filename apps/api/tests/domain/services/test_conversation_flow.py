from app.domain.services.conversation_flow import ConversationFlow
from app.domain.value_objects.conversation_state import ConversationState


def test_next_state_from_greeting():
    flow = ConversationFlow()

    next_state = flow.next_state(ConversationState.GREETING)

    assert next_state == ConversationState.PATIENT_VERIFICATION


def test_next_state_from_patient_verification():
    flow = ConversationFlow()

    next_state = flow.next_state(
        ConversationState.PATIENT_VERIFICATION
    )

    assert next_state == ConversationState.SYMPTOM_COLLECTION