from app.domain.ports.voice_provider import VoiceProvider


class FakeVoiceProvider(VoiceProvider):
    """
    Test double for the VoiceProvider port.
    """

    def __init__(self) -> None:
        self.last_audio: bytes | None = None
        self.last_mime_type: str | None = None

    def transcribe(
        self,
        *,
        audio: bytes,
        mime_type: str,
    ) -> str:
        self.last_audio = audio
        self.last_mime_type = mime_type

        return "Tengo fiebre desde ayer después de la cirugía."
