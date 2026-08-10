from unittest.mock import Mock, patch

import pytest

from app.infrastructure.llm.gemini_language_model import (
    GeminiLanguageModel,
)


def test_gemini_language_model_requires_api_key() -> None:
    with patch.dict(
        "os.environ",
        {},
        clear=True,
    ), pytest.raises(ValueError, match="GEMINI_API_KEY"):
        GeminiLanguageModel()


def test_gemini_language_model_generates_response() -> None:
    fake_response = Mock()
    fake_response.text = "Respuesta generada por Gemini."

    fake_client = Mock()
    fake_client.models.generate_content.return_value = fake_response

    with patch(
        "app.infrastructure.llm.gemini_language_model.genai.Client",
        return_value=fake_client,
    ):
        language_model = GeminiLanguageModel(
            api_key="test-api-key",
        )

        result = language_model.generate(
            prompt="Paciente con fiebre.",
        )

    assert result.content == "Respuesta generada por Gemini."
    assert result.evidence_used == ()

    fake_client.models.generate_content.assert_called_once_with(
        model="gemini-3.5-flash",
        contents="Paciente con fiebre.",
    )