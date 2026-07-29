import pytest

from app.domain.value_objects.evidence import Evidence


def test_evidence_creation():
    evidence = Evidence(
        document_name="postoperative_guidelines.pdf",
        section="3.2",
        chunk_id="chunk-001",
        score=0.95,
    )

    assert evidence.document_name == "postoperative_guidelines.pdf"
    assert evidence.section == "3.2"
    assert evidence.chunk_id == "chunk-001"
    assert evidence.score == 0.95


def test_invalid_score_raises_error():
    with pytest.raises(ValueError):
        Evidence(
            document_name="guide.pdf",
            section="1.1",
            chunk_id="chunk-01",
            score=1.5,
        )


def test_negative_score_raises_error():
    with pytest.raises(ValueError):
        Evidence(
            document_name="guide.pdf",
            section="1.1",
            chunk_id="chunk-01",
            score=-0.1,
        )