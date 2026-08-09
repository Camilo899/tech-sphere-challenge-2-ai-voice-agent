from collections.abc import Sequence

import chromadb

from app.domain.ports.knowledge_indexer import KnowledgeIndexer


class ChromaKnowledgeIndexer(KnowledgeIndexer):
    """Knowledge indexer backed by a local ChromaDB collection."""

    def __init__(
        self,
        *,
        path: str = "./chroma",
        collection_name: str = "clinical_knowledge",
        embedding_provider,
    ) -> None:
        self._embedding_provider = embedding_provider
        self._client = chromadb.PersistentClient(path=path)
        self._collection = self._client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def index(
        self,
        *,
        document_name: str,
        section: str,
        chunk_id: str,
        text: str,
    ) -> None:
        embedding: Sequence[float] = self._embedding_provider(text)

        self._collection.upsert(
            ids=[chunk_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[
                {
                    "document_name": document_name,
                    "section": section,
                }
            ],
        )

    def delete_document(
        self,
        document_name: str,
    ) -> None:
        self._collection.delete(
            where={"document_name": document_name},
        )