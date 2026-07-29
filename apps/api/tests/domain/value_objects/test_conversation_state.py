from app.domain.value_objects.conversation_state import ConversationState


def test_conversation_states_are_defined():
    assert ConversationState.GREETING.value == "greeting"
    assert ConversationState.PATIENT_VERIFICATION.value == "patient_verification"
    assert ConversationState.SYMPTOM_COLLECTION.value == "symptom_collection"
    assert ConversationState.CLINICAL_REASONING.value == "clinical_reasoning"
    assert ConversationState.FINISHED.value == "finished"