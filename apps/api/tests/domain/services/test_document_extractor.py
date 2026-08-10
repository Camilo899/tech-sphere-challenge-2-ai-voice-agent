from app.domain.services.document_extractor import DocumentExtractor

def test_extracts_text_from_document_string() -> None:
    extractor = DocumentExtractor()
    text = extractor.extract("Texto clínico simulado.")
    assert text == "Texto clínico simulado."
