from typing import Any, cast

import chromadb

from app.domain.ports.knowledge_provider import KnowledgeProvider
from app.domain.value_objects.evidence import Evidence
from app.infrastructure.rag.embedding import EmbeddingProvider


class ChromaKnowledgeProvider(KnowledgeProvider):
    """Knowledge provider backed by a local ChromaDB collection."""

    def __init__(
        self,
        *,
        path: str = "./chroma",
        collection_name: str = "clinical_knowledge",
        embedding_provider: EmbeddingProvider,
        n_results: int = 1,
    ) -> None:
        self._embedding_provider = embedding_provider
        self._client = chromadb.PersistentClient(path=path)
        self._collection = self._client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        self._n_results = n_results

    def retrieve(
        self,
        query: str,
    ) -> list[Evidence]:
        query_embedding = self._embedding_provider(query)

        result = self._collection.query(
            query_embeddings=[query_embedding],
            n_results=self._n_results,
        )

        documents = cast(
            list[list[str]],
            result["documents"],
        )[0]

        metadatas = cast(
            list[list[dict[str, Any]]],
            result["metadatas"],
        )[0]

        ids = cast(
            list[list[str]],
            result["ids"],
        )[0]

        distances = cast(
            list[list[float]],
            result["distances"],
        )[0]

        return [
            Evidence(
                document_name=str(metadata["document_name"]),
                section=str(metadata["section"]),
                chunk_id=str(chunk_id),
                text=document,
                score=max(
                    0.0,
                    min(1.0, 1.0 - float(distance)),
                ),
            )
            for document, metadata, chunk_id, distance in zip(
                documents,
                metadatas,
                ids,
                distances,
                strict=True,
            )
        ]