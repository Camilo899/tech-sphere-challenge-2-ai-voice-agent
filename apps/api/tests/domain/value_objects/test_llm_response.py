from app.domain.value_objects.llm_response import LLMResponse


def test_llm_response_stores_content_and_evidence() -> None:
    response = LLMResponse(
        content="Se recomienda valoración clínica.",
        evidence_used=("chunk-001",),
    )

    assert response.content == "Se recomienda valoración clínica."
    assert response.evidence_used == ("chunk-001",)