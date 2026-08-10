from app.domain.services.document_chunker import DocumentChunker


def test_chunks_document_text_in_order() -> None:
    chunker = DocumentChunker(chunk_size=20)

    chunks = chunker.chunk(
        "Primera sección clínica. "
        "Segunda sección clínica."
    )

    assert chunks == [
        "Primera sección",
        "clínica. Segunda",
        "sección clínica.",
    ]