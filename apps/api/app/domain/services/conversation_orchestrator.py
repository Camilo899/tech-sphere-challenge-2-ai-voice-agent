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
from app.domain.services.conversation_analysis_service import (
    ConversationAnalysisService,
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
        conversation_analysis_service: (
            ConversationAnalysisService | None
        ) = None,
    ) -> None:
        self._decision_engine = decision_engine
        self._conversation_flow = conversation_flow
        self._knowledge_service = knowledge_service
        self._clinical_query_builder = clinical_query_builder
        self._clinical_response_service = clinical_response_service
        self._conversation_analysis_service = (
            conversation_analysis_service
            if conversation_analysis_service is not None
            else ConversationAnalysisService()
        )

    def process(
        self,
        context: ConversationContext,
        message: ConversationMessage,
    ) -> ConversationContext:
        context.add_message(message)

        symptoms = self._conversation_analysis_service.extract_symptoms(
            message.content,
        )

        context.symptoms = symptoms

        risk_level = self._conversation_analysis_service.assess_risk(
            symptoms,
        )

        context.clinical_decision = self._decision_engine.decide(
            risk_level,
        )

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

        context.current_state = self._conversation_flow.next_state(
            context.current_state,
        )

        return context