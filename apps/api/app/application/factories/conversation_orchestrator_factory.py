from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)
from app.domain.services.conversation_flow import (
    ConversationFlow,
)
from app.domain.services.conversation_orchestrator import (
    ConversationOrchestrator,
)
from app.domain.services.decision_engine import (
    DecisionEngine,
)


def create_conversation_orchestrator() -> ConversationOrchestrator:
    """
    Creates a fully configured
    ConversationOrchestrator.
    """

    provider = FakeKnowledgeProvider()

    knowledge_service = ClinicalKnowledgeService(
        provider,
    )

    return ConversationOrchestrator(
        decision_engine=DecisionEngine(),
        conversation_flow=ConversationFlow(),
        knowledge_service=knowledge_service,
    )