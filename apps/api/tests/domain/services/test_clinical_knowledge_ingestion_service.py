from app.domain.services.clinical_knowledge_ingestion_service import (
    ClinicalKnowledgeIngestionService,
)


class FakeKnowledgeIndexer:
    def __init__(self) -> None:
        self.indexed_chunks: list[dict[str, str]] = []

    def index(
        self,
        *,
        document_name: str,
        section: str,
        chunk_id: str,
        text: str,
    ) -> None:
        self.indexed_chunks.append(
            {
                "document_name": document_name,
                "section": section,
                "chunk_id": chunk_id,
                "text": text,
            }
        )

    def delete_document(self, document_name: str) -> None:
        pass


def test_ingest_knowledge_chunk_delegates_to_indexer() -> None:
    indexer = FakeKnowledgeIndexer()

    service = ClinicalKnowledgeIngestionService(
        indexer,
    )

    service.ingest_chunk(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-001",
        text="La fiebre después de una cirugía puede requerir valoración clínica.",
    )

    assert indexer.indexed_chunks == [
        {
            "document_name": "clinical-guide",
            "section": "postoperative-follow-up",
            "chunk_id": "chunk-001",
            "text": "La fiebre después de una cirugía puede requerir valoración clínica.",
        }
    ]