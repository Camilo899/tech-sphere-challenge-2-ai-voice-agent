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

    def retrieve(
        self,
        query: str,
    ) -> list[Evidence]:
        return [
            Evidence(
                document_name="clinical-guide",
                section="postoperative-follow-up",
                chunk_id="chunk-001",
                score=0.95,
            ),
        ]