from collections.abc import Sequence
from typing import Protocol


class EmbeddingProvider(Protocol):
    """Generates vector embeddings for text."""

    def __call__(self, text: str) -> Sequence[float]:
        """Return the embedding vector for the given text."""