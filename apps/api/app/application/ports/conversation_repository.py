from typing import Protocol

from app.domain.entities.conversation_context import (
    ConversationContext,
)


class ConversationRepository(Protocol):
    """
    Defines the persistence contract for
    conversation contexts.
    """

    def save(
        self,
        context: ConversationContext,
    ) -> None:
        """
        Persists a conversation context.
        """
        ...