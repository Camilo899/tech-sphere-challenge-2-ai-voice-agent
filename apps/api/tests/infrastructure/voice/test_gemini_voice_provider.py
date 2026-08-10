from unittest.mock import Mock, patch

from app.infrastructure.voice.gemini_voice_provider import (
    GeminiVoiceProvider,
)


def test_gemini_voice_provider_transcribes_audio() -> None:
    fake_response = Mock()
    fake_response.text = "Tengo fiebre desde ayer."

    fake_client = Mock()
    fake_client.models.generate_content.return_value = fake_response

    with patch(
        "app.infrastructure.voice.gemini_voice_provider.genai.Client",
        return_value=fake_client,
    ):
        provider = GeminiVoiceProvider(
            api_key="test-api-key",
        )

        result = provider.transcribe(
            audio=b"fake-audio",
            mime_type="audio/wav",
        )

    assert result == "Tengo fiebre desde ayer."

    fake_client.models.generate_content.assert_called_once()

    call = fake_client.models.generate_content.call_args

    assert call.kwargs["model"] == "gemini-3.6-flash"
    assert call.kwargs["contents"][1].startswith(
        "Transcribe exactly what the patient says."
    )
