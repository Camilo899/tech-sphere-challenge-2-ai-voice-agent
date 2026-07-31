from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.use_cases.start_follow_up import (
    StartFollowUpUseCase,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.conversation_state import (
    ConversationState,
)


def test_start_follow_up_creates_initial_context():
    repository = FakeConversationRepository()

    use_case = StartFollowUpUseCase(repository)

    context = use_case.execute(
        conversation_id="conv-001",
    )

    assert context.conversation_id == "conv-001"

    assert (
        context.current_state
        == ConversationState.GREETING
    )

    assert (
        context.clinical_decision
        == ClinicalDecision.CONTINUE
    )

    assert context.messages == []

    assert context.symptoms == []

    assert context.evidences == []

    assert len(repository.saved_contexts) == 1

    assert (
        repository.saved_contexts[0].conversation_id
        == "conv-001"
    )