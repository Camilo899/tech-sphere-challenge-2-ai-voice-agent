from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ConversationMessage:
    """
    Represents a single message exchanged during
    a postoperative follow-up conversation.
    """

    speaker: str
    content: str
    timestamp: datetime