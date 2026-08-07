from collections.abc import Sequence

from app.infrastructure.rag.bge_embedding_provider import BGEEmbeddingProvider


class FakeEmbeddingModel:
    def __init__(self) -> None:
        self.received_text: str | None = None
        self.received_normalize: bool | None = None

    def encode(
        self,
        text: str,
        *,
        normalize_embeddings: bool,
    ) -> Sequence[float]:
        self.received_text = text
        self.received_normalize = normalize_embeddings

        return [0.1, 0.2, 0.3]


def test_bge_embedding_provider_returns_embedding() -> None:
    model = FakeEmbeddingModel()
    provider = BGEEmbeddingProvider(model=model)

    result = provider("El paciente presenta dolor.")

    assert result == [0.1, 0.2, 0.3]


def test_bge_embedding_provider_passes_text_to_model() -> None:
    model = FakeEmbeddingModel()
    provider = BGEEmbeddingProvider(model=model)

    provider("El paciente presenta fiebre.")

    assert model.received_text == "El paciente presenta fiebre."


def test_bge_embedding_provider_normalizes_embeddings() -> None:
    model = FakeEmbeddingModel()
    provider = BGEEmbeddingProvider(model=model)

    provider("Dolor postoperatorio.")

    assert model.received_normalize is True
