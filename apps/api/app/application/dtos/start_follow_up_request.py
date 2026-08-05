from dataclasses import dataclass


@dataclass(frozen=True)
class StartFollowUpRequest:
    """
    Input model for starting
    a follow-up conversation.
    """

    patient_id: str