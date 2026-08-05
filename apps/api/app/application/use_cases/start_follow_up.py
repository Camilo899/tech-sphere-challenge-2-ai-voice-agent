from app.application.dtos.start_follow_up_request import (
    StartFollowUpRequest,
)
from app.application.dtos.start_follow_up_response import (
    StartFollowUpResponse,
)
from app.application.ports.conversation_repository import (
    ConversationRepository,
)
from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.conversation_state import (
    ConversationState,
)


class StartFollowUpUseCase:
    """
    Initializes a new postoperative follow-up conversation.
    """

    def __init__(
        self,
        repository: ConversationRepository,
    ) -> None:
        self._repository = repository

    def execute(
        self,
        request: StartFollowUpRequest,
    ) -> StartFollowUpResponse:
        context = ConversationContext(
            conversation_id=request.patient_id,
            current_state=ConversationState.GREETING,
            clinical_decision=ClinicalDecision.CONTINUE,
        )

        self._repository.save(context)

        return StartFollowUpResponse(
            conversation_id=context.conversation_id,
            current_state=context.current_state.value,
        )