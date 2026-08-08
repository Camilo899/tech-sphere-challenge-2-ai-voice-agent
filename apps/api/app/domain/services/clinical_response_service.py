from app.domain.ports.language_model import LanguageModel
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)
from app.domain.services.clinical_prompt_builder import (
    ClinicalPromptBuilder,
)
from app.domain.value_objects.llm_response import LLMResponse


class ClinicalResponseService:
    """
    Coordinates clinical evidence retrieval,
    prompt construction, and language model generation.
    """

    def __init__(
        self,
        knowledge_service: ClinicalKnowledgeService,
        prompt_builder: ClinicalPromptBuilder,
        language_model: LanguageModel,
    ) -> None:
        self._knowledge_service = knowledge_service
        self._prompt_builder = prompt_builder
        self._language_model = language_model

    def generate_response(
        self,
        patient_message: str,
    ) -> LLMResponse:
        evidence = self._knowledge_service.retrieve_evidence(
            patient_message,
        )

        prompt = self._prompt_builder.build(
            patient_message=patient_message,
            evidence=evidence,
        )

        return self._language_model.generate(
            prompt=prompt,
        )