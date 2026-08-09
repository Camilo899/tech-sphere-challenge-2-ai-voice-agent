from app.infrastructure.rag.chroma_knowledge_indexer import (
    ChromaKnowledgeIndexer,
)


def test_index_stores_knowledge_chunk(tmp_path) -> None:
    indexer = ChromaKnowledgeIndexer(
        path=str(tmp_path / "chroma"),
        embedding_provider=lambda text: [1.0, 0.0, 0.0],
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-001",
        text="La fiebre después de una cirugía puede requerir valoración clínica.",
    )