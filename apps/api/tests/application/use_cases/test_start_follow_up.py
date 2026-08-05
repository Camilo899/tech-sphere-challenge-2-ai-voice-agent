from app.application.dtos.start_follow_up_request import (
    StartFollowUpRequest,
)
from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.use_cases.start_follow_up import (
    StartFollowUpUseCase,
)


def test_start_follow_up_creates_initial_context():
    repository = FakeConversationRepository()

    use_case = StartFollowUpUseCase(repository)

    request = StartFollowUpRequest(
        patient_id="patient-001",
    )

    response = use_case.execute(request)

    assert response.conversation_id == "patient-001"

    assert response.current_state == "greeting"