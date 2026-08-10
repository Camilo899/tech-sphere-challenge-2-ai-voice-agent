from app.infrastructure.rag.bge_embedding_provider import (
    BGEEmbeddingProvider,
)
from app.infrastructure.rag.chroma_knowledge_indexer import (
    ChromaKnowledgeIndexer,
)
from app.infrastructure.rag.chroma_knowledge_provider import (
    ChromaKnowledgeProvider,
)


def test_bge_embedding_provider_works_with_chroma(
    tmp_path,
) -> None:
    embedding_provider = BGEEmbeddingProvider(
        model=FakeEmbeddingModel(),
    )

    indexer = ChromaKnowledgeIndexer(
        path=str(tmp_path / "chroma"),
        embedding_provider=embedding_provider,
    )

    provider = ChromaKnowledgeProvider(
        path=str(tmp_path / "chroma"),
        embedding_provider=embedding_provider,
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-001",
        text="La fiebre después de una cirugía puede requerir valoración clínica.",
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-002",
        text="El dolor postoperatorio debe ser evaluado según su intensidad.",
    )

    evidence = provider.retrieve(
        "fiebre después de cirugía",
    )

    assert len(evidence) == 1
    assert evidence[0].document_name == "clinical-guide"
    assert evidence[0].section == "postoperative-follow-up"
    assert evidence[0].chunk_id == "chunk-001"


def fake_embedding(text: str) -> list[float]:
    normalized = text.lower()

    if "fiebre" in normalized:
        return [1.0, 0.0, 0.0]

    if "dolor" in normalized:
        return [0.0, 1.0, 0.0]

    return [0.0, 0.0, 1.0]


def test_retrieve_returns_most_relevant_clinical_evidence(
    tmp_path,
):
    indexer = ChromaKnowledgeIndexer(
        path=str(tmp_path / "chroma"),
        embedding_provider=fake_embedding,
    )

    provider = ChromaKnowledgeProvider(
        path=str(tmp_path / "chroma"),
        embedding_provider=fake_embedding,
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-001",
        text="La fiebre después de una cirugía puede requerir valoración clínica.",
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-002",
        text="El dolor postoperatorio debe ser evaluado según su intensidad.",
    )

    evidence = provider.retrieve(
        "fiebre después de cirugía",
    )

    assert len(evidence) == 1

    assert evidence[0].document_name == "clinical-guide"
    assert evidence[0].section == "postoperative-follow-up"
    assert evidence[0].chunk_id == "chunk-001"
    assert 0.0 <= evidence[0].score <= 1.0


class FakeEmbeddingModel:
    def encode(
        self,
        text: str,
        *,
        normalize_embeddings: bool,
    ) -> list[float]:
        if "fiebre" in text.lower():
            return [1.0, 0.0, 0.0]

        if "dolor" in text.lower():
            return [0.0, 1.0, 0.0]

        return [0.0, 0.0, 1.0]