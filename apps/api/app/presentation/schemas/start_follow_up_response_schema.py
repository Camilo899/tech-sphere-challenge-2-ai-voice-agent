from pydantic import BaseModel


class StartFollowUpResponseSchema(BaseModel):
    """
    HTTP response schema returned when
    a follow-up conversation starts.
    """

    conversation_id: str

    current_state: str