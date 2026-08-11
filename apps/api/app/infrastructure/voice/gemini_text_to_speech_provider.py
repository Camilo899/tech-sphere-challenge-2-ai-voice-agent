import os

from google import genai
from google.genai import types

from app.domain.ports.text_to_speech_provider import (
    TextToSpeechProvider,
)


class GeminiTextToSpeechProvider(TextToSpeechProvider):
    """Text-to-speech provider backed by Gemini."""

    def __init__(
        self,
        *,
        model: str = "gemini-3.1-flash-tts-preview",
        voice_name: str = "Kore",
        api_key: str | None = None,
    ) -> None:
        self._model = model
        self._voice_name = voice_name

        resolved_api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not resolved_api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is required."
            )

        self._client = genai.Client(
            api_key=resolved_api_key,
        )

    def synthesize(
        self,
        *,
        text: str,
    ) -> bytes:
        response = self._client.models.generate_content(
            model=self._model,
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=self._voice_name,
                        )
                    )
                ),
            ),
        )

        # Comprobaciones explícitas para evitar None
        if not response or not response.candidates:
            return b""

        candidate = response.candidates[0]
        if not candidate or not candidate.content or not candidate.content.parts:
            return b""

        part = candidate.content.parts[0]
        inline_data = getattr(part, "inline_data", None)
        if inline_data is None:
            return b""

        data: bytes | None = getattr(inline_data, "data", None)
        if data is None:
            return b""

        return data
