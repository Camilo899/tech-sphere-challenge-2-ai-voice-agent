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
        conversation_id: str,
    ) -> ConversationContext:
        context = ConversationContext(
            conversation_id=conversation_id,
            current_state=ConversationState.GREETING,
            clinical_decision=ClinicalDecision.CONTINUE,
        )

        self._repository.save(context)

        return context