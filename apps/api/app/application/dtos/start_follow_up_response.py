from dataclasses import dataclass


@dataclass(frozen=True)
class StartFollowUpResponse:
    """
    Output model returned when a
    follow-up conversation starts.
    """

    conversation_id: str

    current_state: str