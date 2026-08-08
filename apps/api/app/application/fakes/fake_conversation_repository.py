from app.application.ports.conversation_repository import (
    ConversationRepository,
)
from app.domain.entities.conversation_context import (
    ConversationContext,
)


class FakeConversationRepository(ConversationRepository):
    """
    Fake repository used for unit testing.
    """

    def __init__(self) -> None:
        self.saved_contexts: list[ConversationContext] = []

    def save(
        self,
        context: ConversationContext,
    ) -> None:
        self.saved_contexts.append(context)

    def get(
        self,
        conversation_id: str,
    ) -> ConversationContext:
        for context in reversed(self.saved_contexts):
            if context.conversation_id == conversation_id:
                return context

        raise ValueError(
            f"Conversation not found: {conversation_id}"
        )
