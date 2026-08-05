from pydantic import BaseModel


class StartFollowUpRequestSchema(BaseModel):
    """
    HTTP request schema for starting
    a follow-up conversation.
    """

    patient_id: str