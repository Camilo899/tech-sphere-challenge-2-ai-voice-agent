from datetime import UTC, datetime
from app.application.dtos.send_message_response import SendMessageResponse
from app.application.ports.conversation_repository import (
    ConversationRepository,
)
from app.domain.ports.voice_provider import VoiceProvider
from app.domain.services.conversation_orchestrator import (
    ConversationOrchestrator,
)
from app.domain.value_objects.conversation_message import ConversationMessage

class SendVoiceMessageUseCase:
    """
    Transcribes a patient's voice message and processes it
    through the existing clinical conversation flow.
    """

    def __init__(
        self,
        repository: ConversationRepository,
        orchestrator: ConversationOrchestrator,
        voice_provider: VoiceProvider,
    ) -> None:
        self._repository = repository
        self._orchestrator = orchestrator
        self._voice_provider = voice_provider

    def execute(
        self,
        *,
        conversation_id: str,
        audio: bytes,
        mime_type: str,
    ) -> SendMessageResponse:
        transcript = self._voice_provider.transcribe(
            audio=audio,
            mime_type=mime_type,
        )

        context = self._repository.get(
            conversation_id,
        )

        message = ConversationMessage(
            speaker="patient",
            content=transcript,
            timestamp=datetime.now(UTC),
        )

        updated_context = self._orchestrator.process(
            context=context,
            message=message,
        )

        self._repository.save(updated_context)

        assistant_response = ""

        for conversation_message in reversed(
            updated_context.messages,
        ):
            if conversation_message.speaker == "assistant":
                assistant_response = conversation_message.content
                break

        return SendMessageResponse(
            response=assistant_response,
            current_state=updated_context.current_state.value,
            clinical_decision=updated_context.clinical_decision.value,
        )
