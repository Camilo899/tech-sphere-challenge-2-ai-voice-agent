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


def test_delete_document_keeps_chunks_from_other_documents(tmp_path) -> None:
    indexer = ChromaKnowledgeIndexer(
        path=str(tmp_path / "chroma"),
        embedding_provider=lambda text: [1.0, 0.0, 0.0],
    )

    indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-001",
        text="Contenido de guía clínica.",
    )

    indexer.index(
        document_name="medication-guide",
        section="medications",
        chunk_id="chunk-002",
        text="Contenido de medicamentos.",
    )

    indexer.delete_document("clinical-guide")

    result = indexer._collection.get()

    assert result["ids"] == ["chunk-002"]
