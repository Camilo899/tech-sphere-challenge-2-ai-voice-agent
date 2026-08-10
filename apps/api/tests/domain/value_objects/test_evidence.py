import pytest

from app.domain.value_objects.evidence import Evidence


def test_evidence_stores_clinical_metadata_and_text() -> None:
    evidence = Evidence(
        document_name="postoperative_guidelines.pdf",
        section="3.2",
        chunk_id="chunk-001",
        text="La fiebre postoperatoria requiere valoración clínica.",
        score=0.95,
    )

    assert evidence.document_name == "postoperative_guidelines.pdf"
    assert evidence.section == "3.2"
    assert evidence.chunk_id == "chunk-001"
    assert evidence.text == (
        "La fiebre postoperatoria requiere valoración clínica."
    )
    assert evidence.score == 0.95


def test_score_above_one_raises_error() -> None:
    with pytest.raises(ValueError):
        Evidence(
            document_name="guide.pdf",
            section="1.1",
            chunk_id="chunk-01",
            text="Clinical guidance text.",
            score=1.5,
        )


def test_negative_score_raises_error() -> None:
    with pytest.raises(ValueError):
        Evidence(
            document_name="guide.pdf",
            section="1.1",
            chunk_id="chunk-01",
            text="Clinical guidance text.",
            score=-0.1,
        )