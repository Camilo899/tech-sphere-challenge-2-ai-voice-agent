from app.infrastructure.rag.bge_embedding_provider import (
BGEEmbeddingProvider,
)
from app.infrastructure.rag.chroma_knowledge_indexer import (
ChromaKnowledgeIndexer,
)
from app.infrastructure.rag.chroma_knowledge_provider import (
ChromaKnowledgeProvider,
)

def test_bge_embedding_provider_works_with_chroma(tmp_path) -> None:
    embedding_provider = BGEEmbeddingProvider()


    chroma_path = str(tmp_path / "chroma")

    indexer = ChromaKnowledgeIndexer(
        path=chroma_path,
        embedding_provider=embedding_provider,
    )

    provider = ChromaKnowledgeProvider(
        path=chroma_path,
        embedding_provider=embedding_provider,
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-fever",
        text="La fiebre después de una cirugía puede requerir valoración clínica.",
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-pain",
        text="El dolor postoperatorio debe ser evaluado según su intensidad.",
    )

    evidence = provider.retrieve(
        "El paciente presenta fiebre después de una cirugía.",
    )

    assert evidence
    assert evidence[0].document_name == "clinical-guide"
    assert evidence[0].section == "postoperative-follow-up"
    assert evidence[0].chunk_id == "chunk-fever"
    assert 0.0 <= evidence[0].score <= 1.0
