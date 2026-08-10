from app.domain.services.clinical_knowledge_ingestion_service import (
    ClinicalKnowledgeIngestionService,
)
from app.domain.services.clinical_knowledge_service import (
    ClinicalKnowledgeService,
)
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


def test_create_chroma_knowledge_stack_shares_collection(
    tmp_path,
) -> None:
    stack = create_chroma_knowledge_stack(
        path=str(tmp_path / "chroma"),
    )

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


def test_create_chroma_knowledge_stack_supports_ingest_and_retrieve(
    tmp_path,
) -> None:
    stack = create_chroma_knowledge_stack(
        path=str(tmp_path / "chroma"),
    )

    stack.indexer.index(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-ingestion-001",
        text="La fiebre después de una cirugía puede requerir valoración clínica.",
    )

    evidence = stack.provider.retrieve(
        "fiebre después de cirugía",
    )

    assert evidence
    assert evidence[0].document_name == "clinical-guide"
    assert evidence[0].section == "postoperative-follow-up"
    assert evidence[0].chunk_id == "chunk-ingestion-001"
    assert 0.0 <= evidence[0].score <= 1.0


def test_rag_stack_supports_ingestion_and_retrieval(
    tmp_path,
) -> None:
    stack = create_chroma_knowledge_stack(
        path=str(tmp_path / "chroma"),
    )

    ingestion_service = ClinicalKnowledgeIngestionService(
        stack.indexer,
    )

    knowledge_service = ClinicalKnowledgeService(
        stack.provider,
    )

    ingestion_service.ingest_chunk(
        document_name="clinical-guide",
        section="postoperative-follow-up",
        chunk_id="chunk-integration-fever",
        text=(
            "La fiebre después de una cirugía "
            "puede requerir valoración clínica."
        ),
    )

    evidence = knowledge_service.retrieve_evidence(
        "fiebre después de cirugía",
    )

    assert evidence
    assert evidence[0].document_name == "clinical-guide"
    assert evidence[0].section == "postoperative-follow-up"
    assert evidence[0].chunk_id == "chunk-integration-fever"