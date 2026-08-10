from app.application.factories.conversation_orchestrator_factory import (
    create_conversation_orchestrator,
)
from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.use_cases.send_message import SendMessageUseCase
from app.application.use_cases.send_voice_message import (
    SendVoiceMessageUseCase,
)
from app.application.use_cases.start_follow_up import StartFollowUpUseCase
from app.infrastructure.llm.gemini_language_model import (
    GeminiLanguageModel,
)
from app.infrastructure.voice.gemini_voice_provider import (
    GeminiVoiceProvider,
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
    Creates the SendMessageUseCase with the configured
    production LLM.
    """
    language_model = GeminiLanguageModel()

    orchestrator = create_conversation_orchestrator(
        language_model=language_model,
    )

    return SendMessageUseCase(
        repository=_repository,
        orchestrator=orchestrator,
    )


def get_send_voice_message_use_case() -> SendVoiceMessageUseCase:
    """
    Creates the SendVoiceMessageUseCase with the configured
    production voice provider and LLM.
    """
    language_model = GeminiLanguageModel()

    orchestrator = create_conversation_orchestrator(
        language_model=language_model,
    )

    voice_provider = GeminiVoiceProvider()

    return SendVoiceMessageUseCase(
        repository=_repository,
        orchestrator=orchestrator,
        voice_provider=voice_provider,
    )