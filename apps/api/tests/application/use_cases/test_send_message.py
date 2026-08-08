from app.application.dtos.send_message_request import (
SendMessageRequest,
)
from app.application.fakes.fake_conversation_repository import (
FakeConversationRepository,
)
from app.application.fakes.fake_knowledge_provider import (
FakeKnowledgeProvider,
)
from app.application.use_cases.send_message import (
SendMessageUseCase,
)
from app.domain.entities.conversation_context import (
ConversationContext,
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
from app.domain.value_objects.clinical_decision import (
ClinicalDecision,
)
from app.domain.value_objects.conversation_state import (
ConversationState,
)

def test_send_message_processes_existing_conversation() -> None:
    repository = FakeConversationRepository()

    
    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    repository.save(context)

    knowledge_service = ClinicalKnowledgeService(
        FakeKnowledgeProvider(),
    )

    orchestrator = ConversationOrchestrator(
        decision_engine=DecisionEngine(),
        conversation_flow=ConversationFlow(),
        knowledge_service=knowledge_service,
    )

    use_case = SendMessageUseCase(
        repository=repository,
        orchestrator=orchestrator,
    )

    request = SendMessageRequest(
        conversation_id="conv-001",
        message="Tengo fiebre desde ayer.",
    )

    response = use_case.execute(request)

    assert response.current_state == (
        ConversationState.PATIENT_VERIFICATION.value
    )

    assert len(repository.saved_contexts) == 2

    updated_context = repository.saved_contexts[-1]

    assert updated_context.conversation_id == "conv-001"

    assert len(updated_context.messages) == 1

    assert updated_context.messages[0].speaker == "patient"

    assert (
        updated_context.messages[0].content
        == "Tengo fiebre desde ayer."
    )

