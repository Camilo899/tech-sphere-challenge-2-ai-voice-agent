from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.conversation_flow import (
    ConversationFlow,
)
from app.domain.services.decision_engine import (
    DecisionEngine,
)
from app.domain.value_objects.conversation_message import (
    ConversationMessage,
)


class ConversationOrchestrator:
    """
    Coordinates the clinical reasoning
    and conversation progression.
    """

    def __init__(self) -> None:
        self._decision_engine = DecisionEngine()
        self._conversation_flow = ConversationFlow()

    def process(
        self,
        context: ConversationContext,
        message: ConversationMessage,
    ) -> ConversationContext:
        context.add_message(message)

        decision = self._decision_engine.decide_from_context(
            context,
        )

        context.clinical_decision = decision

        context.current_state = (
            self._conversation_flow.next_state(
                context.current_state,
            )
        )

        return context