from app.domain.ports.language_model import LanguageModel
from app.domain.value_objects.evidence import Evidence
from app.domain.value_objects.llm_response import LLMResponse
from app.domain.services.clinical_prompt_builder import ClinicalPromptBuilder


class ClinicalResponseService:
    """
    Coordinates clinical evidence retrieval,
    prompt construction, and language model generation.
    """

    def __init__(
        self,
        prompt_builder: ClinicalPromptBuilder,
        language_model: LanguageModel,
    ) -> None:
        self._prompt_builder = prompt_builder
        self._language_model = language_model

    def generate_response(
        self,
        *,
        patient_message: str,
        evidence: list[Evidence],
    ) -> LLMResponse:
        prompt = self._prompt_builder.build(
            patient_message=patient_message,
            evidence=evidence,
        )

        return self._language_model.generate(
            prompt=prompt,
        )
