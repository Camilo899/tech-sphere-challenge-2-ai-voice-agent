from pydantic import BaseModel


class SendMessageRequestSchema(BaseModel):
    """
    HTTP request schema for sending
    a patient message.
    """

    conversation_id: str

    message: str