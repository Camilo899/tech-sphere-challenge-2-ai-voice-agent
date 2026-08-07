from app.domain.ports.knowledge_provider import (
    KnowledgeProvider,
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
from app.infrastructure.rag.factory import (
    create_chroma_knowledge_provider,
)


def create_conversation_orchestrator(
    knowledge_provider: KnowledgeProvider | None = None,
) -> ConversationOrchestrator:
    """
    Creates a fully configured ConversationOrchestrator.
    """
    provider = (
        knowledge_provider
        if knowledge_provider is not None
        else create_chroma_knowledge_provider()
    )

    knowledge_service = ClinicalKnowledgeService(
        provider,
    )

    return ConversationOrchestrator(
        decision_engine=DecisionEngine(),
        conversation_flow=ConversationFlow(),
        knowledge_service=knowledge_service,
    )