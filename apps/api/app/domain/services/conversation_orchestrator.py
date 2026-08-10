from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)
from app.domain.services.clinical_query_builder import (
    ClinicalQueryBuilder,
)
from app.domain.services.clinical_response_service import (
    ClinicalResponseService,
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
    Coordinates clinical reasoning
    and conversation progression.
    """

    def __init__(
        self,
        decision_engine: DecisionEngine,
        conversation_flow: ConversationFlow,
        knowledge_service: ClinicalKnowledgeService,
        clinical_query_builder: ClinicalQueryBuilder,
        clinical_response_service: ClinicalResponseService | None = None,
    ) -> None:
        self._decision_engine = decision_engine
        self._conversation_flow = conversation_flow
        self._knowledge_service = knowledge_service
        self._clinical_query_builder = clinical_query_builder
        self._clinical_response_service = clinical_response_service

    def process(
        self,
        context: ConversationContext,
        message: ConversationMessage,
    ) -> ConversationContext:
        context.add_message(message)

        query = self._clinical_query_builder.build(context)

        evidence = self._knowledge_service.retrieve_evidence(
            query,
        )

        if self._clinical_response_service is not None:
            response = self._clinical_response_service.generate_response(
                patient_message=message.content,
                evidence=evidence,
            )

            context.evidences = evidence

            context.add_message(
                ConversationMessage(
                    speaker="assistant",
                    content=response.content,
                    timestamp=message.timestamp,
                ),
            )

        decision = self._decision_engine.decide_from_context(
            context,
        )

        context.clinical_decision = decision

        context.current_state = self._conversation_flow.next_state(
            context.current_state,
        )

        return context