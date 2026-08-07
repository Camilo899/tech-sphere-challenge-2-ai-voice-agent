from app.infrastructure.rag.bge_embedding_provider import (
    BGEEmbeddingProvider,
)
from app.infrastructure.rag.chroma_knowledge_provider import (
    ChromaKnowledgeProvider,
)
from app.infrastructure.rag.factory import (
    create_chroma_knowledge_provider,
)


def test_create_chroma_knowledge_provider_uses_real_rag_stack() -> None:
    provider = create_chroma_knowledge_provider()

    assert isinstance(provider, ChromaKnowledgeProvider)
    assert isinstance(
        provider._embedding_provider,
        BGEEmbeddingProvider,
    )