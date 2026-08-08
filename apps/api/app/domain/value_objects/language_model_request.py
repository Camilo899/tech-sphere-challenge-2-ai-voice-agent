from dataclasses import dataclass

from app.domain.value_objects.conversation_message import (
    ConversationMessage,
)
from app.domain.value_objects.evidence import Evidence


@dataclass(frozen=True)
class LanguageModelRequest:
    """
    Represents the context provided to the language model
    for interpreting a conversation turn.
    """

    messages: list[ConversationMessage]
    evidences: list[Evidence]
