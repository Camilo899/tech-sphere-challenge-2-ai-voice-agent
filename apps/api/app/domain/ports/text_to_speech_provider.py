from typing import Protocol


class TextToSpeechProvider(Protocol):
    """Port for text-to-speech capabilities."""

    def synthesize(
        self,
        *,
        text: str,
    ) -> bytes:
        """Converts text into audio bytes."""
        ...