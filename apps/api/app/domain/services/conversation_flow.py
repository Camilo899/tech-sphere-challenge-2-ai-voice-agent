from typing import ClassVar

from app.domain.value_objects.conversation_state import (
    ConversationState,
)


class ConversationFlow:
    """
    Controls the transitions between conversation states.
    """

    _TRANSITIONS: ClassVar[
        dict[ConversationState, ConversationState]
    ] = {
        ConversationState.GREETING:
            ConversationState.PATIENT_VERIFICATION,

        ConversationState.PATIENT_VERIFICATION:
            ConversationState.SYMPTOM_COLLECTION,

        ConversationState.SYMPTOM_COLLECTION:
            ConversationState.CLARIFICATION,

        ConversationState.CLARIFICATION:
            ConversationState.KNOWLEDGE_RETRIEVAL,

        ConversationState.KNOWLEDGE_RETRIEVAL:
            ConversationState.CLINICAL_REASONING,

        ConversationState.CLINICAL_REASONING:
            ConversationState.DECISION,

        ConversationState.DECISION:
            ConversationState.SUMMARY,

        ConversationState.SUMMARY:
            ConversationState.FINISHED,
    }

    def next_state(
        self,
        current_state: ConversationState,
    ) -> ConversationState:
        return self._TRANSITIONS.get(
            current_state,
            ConversationState.FINISHED,
        )