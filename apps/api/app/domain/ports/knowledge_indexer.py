from abc import ABC, abstractmethod


class KnowledgeIndexer(ABC):
    """
    Indexes and removes clinical knowledge.
    """

    @abstractmethod
    def index(
        self,
        *,
        document_name: str,
        section: str,
        chunk_id: str,
        text: str,
    ) -> None:
        """
        Indexes one knowledge chunk.
        """

    @abstractmethod
    def delete_document(
        self,
        document_name: str,
    ) -> None:
        """
        Removes all indexed chunks belonging to a document.
        """
