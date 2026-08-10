from app.domain.ports.knowledge_indexer import KnowledgeIndexer


class ClinicalKnowledgeIngestionService:
    """
    Application service responsible for ingesting clinical knowledge.
    """

    def __init__(
        self,
        knowledge_indexer: KnowledgeIndexer,
    ) -> None:
        self._knowledge_indexer = knowledge_indexer

    def ingest_chunk(
        self,
        *,
        document_name: str,
        section: str,
        chunk_id: str,
        text: str,
    ) -> None:
        """
        Indexes one clinical knowledge chunk.
        """
        self._knowledge_indexer.index(
            document_name=document_name,
            section=section,
            chunk_id=chunk_id,
            text=text,
        )