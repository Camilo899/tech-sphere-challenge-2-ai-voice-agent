from dataclasses import dataclass


@dataclass(frozen=True)
class SendVoiceMessageResponse:
    response: str
    audio: bytes
    current_state: str