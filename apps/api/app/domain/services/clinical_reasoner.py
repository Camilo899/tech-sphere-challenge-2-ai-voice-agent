from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.conversation_flow import (
    ConversationFlow,
)


class ClinicalReasoner:
    """
    Coordinates the clinical conversation flow.
    """

    def __init__(self) -> None:
        self._flow = ConversationFlow()

    def next_step(
        self,
        context: ConversationContext,
    ) -> ConversationContext:
        context.current_state = self._flow.next_state(
            context.current_state
        )

        return context