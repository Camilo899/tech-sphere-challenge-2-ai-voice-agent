from app.domain.ports.language_model import LanguageModel
from app.domain.value_objects.llm_response import LLMResponse


class FakeLanguageModel(LanguageModel):
    """
    Test double for the LanguageModel port.
    """

    def __init__(self) -> None:
        self.last_prompt: str | None = None

    def generate(
        self,
        *,
        prompt: str,
    ) -> LLMResponse:
        self.last_prompt = prompt

        return LLMResponse(
            content="Respuesta clínica simulada.",
            evidence_used=("chunk-001",),
        )