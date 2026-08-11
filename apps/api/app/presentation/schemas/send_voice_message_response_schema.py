from pydantic import BaseModel


class SendVoiceMessageResponseSchema(BaseModel):
    """
    HTTP response schema for a processed voice message.
    """

    response: str
    current_state: str
    audio: str | None = None