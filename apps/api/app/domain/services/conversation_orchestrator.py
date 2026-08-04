from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
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

    def __init__(
        self,
        decision_engine: DecisionEngine,
        conversation_flow: ConversationFlow,
        knowledge_service: ClinicalKnowledgeService,
    ) -> None:
        self._decision_engine = decision_engine
        self._conversation_flow = conversation_flow
        self._knowledge_service = knowledge_service

    def process(
        self,
        context: ConversationContext,
        message: ConversationMessage,
    ) -> ConversationContext:
        context.add_message(message)

        # Por ahora únicamente recuperamos evidencia.
        # En el siguiente incremento la utilizaremos.
        _ = self._knowledge_service.retrieve_evidence(
            message.content,
        )

        decision = (
            self._decision_engine.decide_from_context(
                context,
            )
        )

        context.clinical_decision = decision

        context.current_state = (
            self._conversation_flow.next_state(
                context.current_state,
            )
        )

        return context