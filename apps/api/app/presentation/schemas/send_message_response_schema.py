from pydantic import BaseModel


class SendMessageResponseSchema(BaseModel):
    """
    HTTP response schema returned after
    processing a patient message.
    """

    response: str

    current_state: str