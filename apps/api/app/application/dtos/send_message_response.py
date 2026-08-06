from dataclasses import dataclass


@dataclass(frozen=True)
class SendMessageResponse:
    """
    Output model returned after processing
    a patient message.
    """

    response: str

    current_state: str