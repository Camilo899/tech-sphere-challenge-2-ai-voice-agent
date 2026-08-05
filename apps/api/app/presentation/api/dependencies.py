from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.use_cases.start_follow_up import (
    StartFollowUpUseCase,
)


def get_start_follow_up_use_case() -> StartFollowUpUseCase:
    """
    Creates the StartFollowUpUseCase with its dependencies.
    """
    repository = FakeConversationRepository()

    return StartFollowUpUseCase(repository)