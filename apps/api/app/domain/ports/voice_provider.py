from typing import Protocol


class VoiceProvider(Protocol):
    """
    Port for speech-to-text and text-to-speech capabilities.
    """

    def transcribe(
        self,
        *,
        audio: bytes,
        mime_type: str,
    ) -> str:
        """
        Converts spoken audio into text.
        """
        ...
