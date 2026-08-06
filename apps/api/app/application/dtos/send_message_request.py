from dataclasses import dataclass


@dataclass(frozen=True)
class SendMessageRequest:
    """
    Input model for processing a patient message.
    """

    conversation_id: str

    message: str