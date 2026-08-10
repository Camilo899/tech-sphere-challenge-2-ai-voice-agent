from app.domain.ports.knowledge_provider import (
    KnowledgeProvider,
)
from app.domain.ports.language_model import LanguageModel
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)
from app.domain.services.clinical_prompt_builder import (
    ClinicalPromptBuilder,
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
from app.domain.services.conversation_orchestrator import (
    ConversationOrchestrator,
)
from app.domain.services.decision_engine import (
    DecisionEngine,
)
from app.infrastructure.rag.factory import (
    create_chroma_knowledge_stack,
)


def create_conversation_orchestrator(
    knowledge_provider: KnowledgeProvider | None = None,
    language_model: LanguageModel | None = None,
) -> ConversationOrchestrator:
    """
    Creates a configured ConversationOrchestrator.
    """
    provider = (
        knowledge_provider
        if knowledge_provider is not None
        else create_chroma_knowledge_stack().provider
    )

    knowledge_service = ClinicalKnowledgeService(
        provider,
    )

    clinical_response_service = None

    if language_model is not None:
        clinical_response_service = ClinicalResponseService(
            prompt_builder=ClinicalPromptBuilder(),
            language_model=language_model,
        )

    return ConversationOrchestrator(
        decision_engine=DecisionEngine(),
        conversation_flow=ConversationFlow(),
        knowledge_service=knowledge_service,
        clinical_query_builder=ClinicalQueryBuilder(),
        clinical_response_service=clinical_response_service,
    )