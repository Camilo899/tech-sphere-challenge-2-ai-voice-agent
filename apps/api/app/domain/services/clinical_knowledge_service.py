from app.domain.ports.knowledge_provider import (
    KnowledgeProvider,
)
from app.domain.value_objects.evidence import (
    Evidence,
)


class ClinicalKnowledgeService:
    """
    Domain service responsible for retrieving
    clinical evidence.
    """

    def __init__(
        self,
        knowledge_provider: KnowledgeProvider,
    ) -> None:
        self._knowledge_provider = knowledge_provider

    def retrieve_evidence(
        self,
        query: str,
    ) -> list[Evidence]:
        """
        Retrieves clinical evidence
        for the given query.
        """
        return self._knowledge_provider.retrieve(
            query,
        )