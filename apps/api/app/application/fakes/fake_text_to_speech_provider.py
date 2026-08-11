from app.domain.ports.text_to_speech_provider import TextToSpeechProvider


class FakeTextToSpeechProvider(TextToSpeechProvider):
    """Test double for the TextToSpeechProvider port."""

    def __init__(self) -> None:
        self.last_text: str | None = None

    def synthesize(
        self,
        *,
        text: str,
    ) -> bytes:
        self.last_text = text
        return b"fake-audio:" + text.encode()
