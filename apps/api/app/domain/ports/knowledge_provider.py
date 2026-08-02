from abc import ABC, abstractmethod

from app.domain.value_objects.evidence import (
    Evidence,
)


class KnowledgeProvider(ABC):
    """
    Provides clinical evidence relevant
    to a patient's symptoms.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
    ) -> list[Evidence]:
        """
        Retrieves clinical evidence
        matching the query.
        """