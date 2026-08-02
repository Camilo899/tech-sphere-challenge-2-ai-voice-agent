from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)


def test_retrieve_evidence():
    provider = FakeKnowledgeProvider()

    service = ClinicalKnowledgeService(
        provider,
    )

    evidence = service.retrieve_evidence(
        "fiebre",
    )

    assert len(evidence) == 1

    assert (
        evidence[0].document_name
        == "clinical-guide"
    )

    assert (
        evidence[0].section
        == "postoperative-follow-up"
    )

    assert (
        evidence[0].chunk_id
        == "chunk-001"
    )

    assert evidence[0].score == 0.95