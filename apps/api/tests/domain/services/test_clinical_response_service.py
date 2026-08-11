from app.application.fakes.fake_language_model import (
    FakeLanguageModel,
)
from app.domain.services.clinical_prompt_builder import (
    ClinicalPromptBuilder,
)
from app.domain.services.clinical_response_service import (
    ClinicalResponseService,
)
from app.domain.value_objects.evidence import Evidence


def test_generate_response_uses_retrieved_evidence() -> None:
    language_model = FakeLanguageModel()

    service = ClinicalResponseService(
        prompt_builder=ClinicalPromptBuilder(),
        language_model=language_model,
    )

    evidence = [
        Evidence(
            document_name="postoperative-guide.pdf",
            section="Fever",
            chunk_id="chunk-001",
            text="Postoperative fever may require clinical evaluation.",
            score=0.95,
        ),
    ]

    result = service.generate_response(
        patient_message="Tengo fiebre desde ayer.",
        evidence=evidence,
    )

    assert result.content == "Respuesta clínica simulada."

    assert language_model.last_prompt is not None

    assert "Tengo fiebre desde ayer." in language_model.last_prompt
    assert "postoperative-guide.pdf" in language_model.last_prompt
    assert "chunk-001" in language_model.last_prompt


def test_returns_safe_response_when_no_evidence_is_available() -> None:
    language_model = FakeLanguageModel()

    service = ClinicalResponseService(
        prompt_builder=ClinicalPromptBuilder(),
        language_model=language_model,
    )

    response = service.generate_response(
        patient_message="Tengo fiebre.",
        evidence=[],
    )

    assert (
        response.content
        == "No se encontró evidencia clínica suficiente "
        "para responder de forma segura."
    )

    assert response.evidence_used == ()
    assert language_model.last_prompt is None