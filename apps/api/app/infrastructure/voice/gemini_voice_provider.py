import os

from google import genai
from google.genai import types

from app.domain.ports.voice_provider import VoiceProvider


class GeminiVoiceProvider(VoiceProvider):
    """
    Voice provider backed by Google Gemini audio understanding.
    """

    def __init__(
        self,
        *,
        model: str = "gemini-3.6-flash",
        api_key: str | None = None,
    ) -> None:
        self._model = model

        resolved_api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is required."
            )

        self._client = genai.Client(
            api_key=resolved_api_key,
        )

    def transcribe(
        self,
        *,
        audio: bytes,
        mime_type: str,
    ) -> str:
        response = self._client.models.generate_content(
            model=self._model,
            contents=[
                types.Part.from_bytes(
                    data=audio,
                    mime_type=mime_type,
                ),
                (
                    "Transcribe exactly what the patient says. "
                    "Return only the spoken text in the original language. "
                    "Do not summarize, interpret, or add information."
                ),
            ],
        )

        return response.text or ""
