class DocumentChunker:
    def __init__(self, chunk_size: int) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")

        self._chunk_size = chunk_size

    def chunk(self, text: str) -> list[str]:
        words = text.split()
        chunks: list[str] = []
        current_words: list[str] = []
        current_length = 0

        for word in words:
            additional_length = len(word)
            if current_words:
                additional_length += 1

            if current_words and current_length + additional_length > self._chunk_size:
                chunks.append(" ".join(current_words))
                current_words = []
                current_length = 0

            current_words.append(word)
            current_length += len(word)

            if len(current_words) > 1:
                current_length += 1

        if current_words:
            chunks.append(" ".join(current_words))

        return chunks