from dataclasses import dataclass, field

from app.domain.value_objects.clinical_decision import ClinicalDecision
from app.domain.value_objects.conversation_message import ConversationMessage
from app.domain.value_objects.conversation_state import ConversationState
from app.domain.value_objects.evidence import Evidence


@dataclass
class ConversationContext:
    """
    Represents the current state of a follow-up conversation.
    """

    conversation_id: str

    current_state: ConversationState

    clinical_decision: ClinicalDecision

    symptoms: list[str] = field(default_factory=list)

    evidences: list[Evidence] = field(default_factory=list)

    messages: list[ConversationMessage] = field(default_factory=list)