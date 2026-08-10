from dataclasses import dataclass

from app.infrastructure.rag.bge_embedding_provider import (
    BGEEmbeddingProvider,
)
from app.infrastructure.rag.chroma_knowledge_indexer import (
    ChromaKnowledgeIndexer,
)
from app.infrastructure.rag.chroma_knowledge_provider import (
    ChromaKnowledgeProvider,
)


@dataclass(frozen=True)
class RAGStack:
    provider: ChromaKnowledgeProvider
    indexer: ChromaKnowledgeIndexer


def create_chroma_knowledge_provider() -> ChromaKnowledgeProvider:
    embedding_provider = BGEEmbeddingProvider()

    return ChromaKnowledgeProvider(
        embedding_provider=embedding_provider,
    )


def create_chroma_knowledge_stack(
    *,
    path: str = "./chroma",
    collection_name: str = "clinical_knowledge",
) -> RAGStack:
    embedding_provider = BGEEmbeddingProvider()

    provider = ChromaKnowledgeProvider(
        path=path,
        collection_name=collection_name,
        embedding_provider=embedding_provider,
    )

    indexer = ChromaKnowledgeIndexer(
        path=path,
        collection_name=collection_name,
        embedding_provider=embedding_provider,
    )

    return RAGStack(
        provider=provider,
        indexer=indexer,
    )