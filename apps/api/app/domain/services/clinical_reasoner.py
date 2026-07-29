from app.domain.entities.conversation_context import ConversationContext
from app.domain.value_objects.conversation_state import ConversationState


class ClinicalReasoner:
    """
    Domain service responsible for deciding the next
    step in the follow-up conversation.
    """

    def next_step(
        self,
        context: ConversationContext,
    ) -> ConversationContext:
        if context.current_state == ConversationState.GREETING:
            context.current_state = (
                ConversationState.PATIENT_VERIFICATION
            )

        return context