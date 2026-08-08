from datetime import UTC, datetime

from app.application.dtos.send_message_request import (
    SendMessageRequest,
)
from app.application.dtos.send_message_response import (
    SendMessageResponse,
)
from app.application.ports.conversation_repository import (
    ConversationRepository,
)
from app.domain.services.conversation_orchestrator import (
    ConversationOrchestrator,
)
from app.domain.value_objects.conversation_message import (
    ConversationMessage,
)


class SendMessageUseCase:
    """
    Processes a patient message within
    an existing follow-up conversation.
    """

    def __init__(
        self,
        repository: ConversationRepository,
        orchestrator: ConversationOrchestrator,
    ) -> None:
        self._repository = repository
        self._orchestrator = orchestrator

    def execute(
        self,
        request: SendMessageRequest,
    ) -> SendMessageResponse:
        context = self._repository.get(
            request.conversation_id,
        )

        message = ConversationMessage(
            speaker="patient",
            content=request.message,
            timestamp=datetime.now(UTC),
        )

        updated_context = self._orchestrator.process(
            context=context,
            message=message,
        )

        self._repository.save(updated_context)

        return SendMessageResponse(
            response="",
            current_state=updated_context.current_state.value,
        )