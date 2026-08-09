import os

from google import genai

from app.domain.ports.language_model import LanguageModel
from app.domain.value_objects.llm_response import LLMResponse


class GeminiLanguageModel(LanguageModel):
    """
    LanguageModel adapter backed by Google Gemini.
    """

    def __init__(
        self,
        *,
        model: str = "gemini-1.5-flash",
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

    def generate(
        self,
        *,
        prompt: str,
    ) -> LLMResponse:
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
        )

        content = response.text or ""

        return LLMResponse(
            content=content,
            evidence_used=(),
        )