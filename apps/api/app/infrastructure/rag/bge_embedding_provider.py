from collections.abc import Sequence
from typing import Any

from sentence_transformers import SentenceTransformer

from app.infrastructure.rag.embedding import EmbeddingProvider


class BGEEmbeddingProvider(EmbeddingProvider):
    """Embedding provider backed by BAAI BGE-M3."""

    def __init__(
        self,
        *,
        model_name: str = "BAAI/bge-m3",
        model: Any | None = None,
    ) -> None:
        self._model = model or SentenceTransformer(model_name)

    def __call__(self, text: str) -> Sequence[float]:
        embedding = self._model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist() if hasattr(embedding, "tolist") else embedding