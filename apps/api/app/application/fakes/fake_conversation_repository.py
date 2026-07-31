from app.application.ports.conversation_repository import (
    ConversationRepository,
)
from app.domain.entities.conversation_context import (
    ConversationContext,
)


class FakeConversationRepository(
    ConversationRepository,
):
    """
    Fake repository used for unit testing.
    """

    def __init__(self) -> None:
        self.saved_contexts: list[
            ConversationContext
        ] = []

    def save(
        self,
        context: ConversationContext,
    ) -> None:
        self.saved_contexts.append(context)