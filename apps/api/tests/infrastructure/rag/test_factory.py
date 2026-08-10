from app.infrastructure.rag.bge_embedding_provider import (
    BGEEmbeddingProvider,
)
from app.infrastructure.rag.chroma_knowledge_indexer import (
    ChromaKnowledgeIndexer,
)
from app.infrastructure.rag.chroma_knowledge_provider import (
    ChromaKnowledgeProvider,
)
from app.infrastructure.rag.factory import (
    create_chroma_knowledge_provider,
    create_chroma_knowledge_stack,
)


def test_create_chroma_knowledge_provider_uses_real_rag_stack() -> None:
    provider = create_chroma_knowledge_provider()

    assert isinstance(provider, ChromaKnowledgeProvider)
    assert isinstance(
        provider._embedding_provider,
        BGEEmbeddingProvider,
    )


def test_create_chroma_knowledge_stack_uses_shared_embedding_provider() -> None:
    stack = create_chroma_knowledge_stack()

    assert isinstance(stack.provider, ChromaKnowledgeProvider)
    assert isinstance(stack.indexer, ChromaKnowledgeIndexer)

    assert (
        stack.provider._embedding_provider
        is stack.indexer._embedding_provider
    )

def test_create_chroma_knowledge_stack_shares_collection() -> None:
    stack = create_chroma_knowledge_stack()

    stack.indexer.index(
        document_name="test_document",
        section="test_section",
        chunk_id="test-stack-shared-collection",
        text="El paciente presenta dolor postoperatorio leve.",
    )

    evidence = stack.provider.retrieve(
        "dolor postoperatorio",
    )

    assert evidence
    assert evidence[0].document_name == "test_document"
    assert evidence[0].section == "test_section"
    assert evidence[0].chunk_id == "test-stack-shared-collection"