from app.domain.ports.knowledge_provider import (
    KnowledgeProvider,
)
from app.domain.value_objects.evidence import (
    Evidence,
)


class FakeKnowledgeProvider(KnowledgeProvider):
    """
    Test double for the KnowledgeProvider port.
    """

    def __init__(self) -> None:
        self.last_query: str | None = None

    def retrieve(
        self,
        query: str,
    ) -> list[Evidence]:
        self.last_query = query
        

        return [
            Evidence(
                document_name="clinical-guide",
                section="postoperative-follow-up",
                chunk_id="chunk-001",
                text="La fiebre después de una cirugía puede requerir valoración clínica.",
                score=0.95,
            ),
        ]