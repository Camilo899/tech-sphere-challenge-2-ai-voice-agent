from app.infrastructure.rag.bge_embedding_provider import (
    BGEEmbeddingProvider,
)
from app.infrastructure.rag.chroma_knowledge_provider import (
    ChromaKnowledgeProvider,
)


def create_chroma_knowledge_provider() -> ChromaKnowledgeProvider:
    embedding_provider = BGEEmbeddingProvider()

    return ChromaKnowledgeProvider(
        embedding_provider=embedding_provider,
    )