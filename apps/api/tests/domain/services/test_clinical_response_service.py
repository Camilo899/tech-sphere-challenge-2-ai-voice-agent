from app.application.fakes.fake_language_model import (
    FakeLanguageModel,
)
from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)
from app.domain.services.clinical_prompt_builder import (
    ClinicalPromptBuilder,
)
from app.domain.services.clinical_response_service import (
    ClinicalResponseService,
)


def test_generate_response_uses_retrieved_evidence() -> None:
    knowledge_provider = FakeKnowledgeProvider()
    knowledge_service = ClinicalKnowledgeService(
        knowledge_provider,
    )

    language_model = FakeLanguageModel()

    service = ClinicalResponseService(
        knowledge_service=knowledge_service,
        prompt_builder=ClinicalPromptBuilder(),
        language_model=language_model,
    )

    response = service.generate_response(
        "Tengo fiebre desde ayer.",
    )

    assert response.content == "Respuesta clínica simulada."
    assert response.evidence_used == ("chunk-001",)

    assert language_model.last_prompt is not None
    assert "Tengo fiebre desde ayer." in language_model.last_prompt
    assert "clinical-guide" in language_model.last_prompt
    assert "chunk-001" in language_model.last_prompt