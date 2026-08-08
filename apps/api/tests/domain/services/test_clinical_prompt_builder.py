from app.domain.services.clinical_prompt_builder import (
    ClinicalPromptBuilder,
)
from app.domain.value_objects.evidence import Evidence


def test_build_includes_patient_message_and_evidence() -> None:
    builder = ClinicalPromptBuilder()

    evidence = [
        Evidence(
            document_name="clinical-guide",
            section="postoperative-follow-up",
            chunk_id="chunk-001",
            score=0.95,
        ),
    ]

    prompt = builder.build(
        patient_message="Tengo fiebre desde ayer.",
        evidence=evidence,
    )

    assert "Tengo fiebre desde ayer." in prompt
    assert "clinical-guide" in prompt
    assert "postoperative-follow-up" in prompt
    assert "chunk-001" in prompt
    assert "0.950" in prompt