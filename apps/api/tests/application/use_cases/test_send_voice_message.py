from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)
from app.application.fakes.fake_language_model import FakeLanguageModel

from app.application.fakes.fake_voice_provider import FakeVoiceProvider
from app.application.fakes.fake_text_to_speech_provider import (
    FakeTextToSpeechProvider,
)
from app.application.factories.conversation_orchestrator_factory import (
    create_conversation_orchestrator,
)
from app.application.use_cases.send_voice_message import (
    SendVoiceMessageUseCase,
)
from app.application.use_cases.start_follow_up import StartFollowUpUseCase
from app.application.dtos.start_follow_up_request import StartFollowUpRequest


def test_send_voice_message_processes_transcribed_message() -> None:
    repository = FakeConversationRepository()
    voice_provider = FakeVoiceProvider()
    text_to_speech_provider = FakeTextToSpeechProvider()
    language_model = FakeLanguageModel()
    knowledge_provider = FakeKnowledgeProvider()

    orchestrator = create_conversation_orchestrator(
        knowledge_provider=knowledge_provider,
        language_model=language_model,
    )

    StartFollowUpUseCase(
        repository=repository,
    ).execute(
        StartFollowUpRequest(
            patient_id="patient-001",
        ),
    )

    use_case = SendVoiceMessageUseCase(
        repository=repository,
        orchestrator=orchestrator,
        voice_provider=voice_provider,
        text_to_speech_provider=text_to_speech_provider,
    )

    result = use_case.execute(
        conversation_id="patient-001",
        audio=b"fake-audio",
        mime_type="audio/wav",
    )

    assert result.response == "Respuesta clínica simulada."
    assert result.current_state == "patient_verification"
    assert result.audio is not None
    assert result.audio.startswith(b"fake-audio:")
    assert text_to_speech_provider.last_text == result.response

    assert voice_provider.last_audio == b"fake-audio"
    assert voice_provider.last_mime_type == "audio/wav"

    assert language_model.last_prompt is not None
    assert (
        "Tengo fiebre desde ayer después de la cirugía."
        in language_model.last_prompt
    )
