from app.domain.ports.knowledge_indexer import KnowledgeIndexer
from app.domain.services.clinical_knowledge_ingestion_service import (
    ClinicalKnowledgeIngestionService,
)
from app.domain.services.document_chunker import DocumentChunker
from app.domain.services.document_extractor import DocumentExtractor


class FakeKnowledgeIndexer(KnowledgeIndexer):
    def __init__(self) -> None:
        self.ingested = []

    def index(self, document_name: str, section: str, chunk_id: str, text: str) -> None:
        # Simula la indexación guardando los datos
        self.ingested.append((document_name, section, chunk_id, text))

    def delete_document(self, document_name: str) -> None:
        # Simulación: elimina todos los chunks asociados al documento
        self.ingested = [entry for entry in self.ingested if entry[0] != document_name]


def test_document_ingestion_flow_in_order() -> None:
    extractor = DocumentExtractor()
    chunker = DocumentChunker(chunk_size=15)
    indexer = FakeKnowledgeIndexer()
    ingestion_service = ClinicalKnowledgeIngestionService(indexer)

    # Documento simulado
    document_text = "Primera sección clínica. Segunda sección clínica."
    extracted_text = extractor.extract(document_text)
    chunks = chunker.chunk(extracted_text)

    # Ingestar cada chunk
    for i, chunk in enumerate(chunks):
        ingestion_service.ingest_chunk(
            document_name="doc1",
            section="clinical",
            chunk_id=str(i),
            text=chunk,
        )

    # Verificar que los chunks fueron recibidos en orden
    assert [text for (_, _, _, text) in indexer.ingested] == chunks
