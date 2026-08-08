from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.use_cases.send_message import (
    SendMessageUseCase,
)
from app.application.use_cases.start_follow_up import (
    StartFollowUpUseCase,
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
from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)


_repository = FakeConversationRepository()


def get_start_follow_up_use_case() -> StartFollowUpUseCase:
    """
    Creates the StartFollowUpUseCase with shared
    in-memory repository.
    """
    return StartFollowUpUseCase(_repository)


def get_send_message_use_case() -> SendMessageUseCase:
    """
    Creates the SendMessageUseCase with shared
    conversation dependencies.
    """
    knowledge_service = ClinicalKnowledgeService(
        FakeKnowledgeProvider(),
    )

    orchestrator = ConversationOrchestrator(
        decision_engine=DecisionEngine(),
        conversation_flow=ConversationFlow(),
        knowledge_service=knowledge_service,
    )

    return SendMessageUseCase(
        repository=_repository,
        orchestrator=orchestrator,
    )
