import pytest

from app.domain.ports.knowledge_provider import (
    KnowledgeProvider,
)


def test_knowledge_provider_is_abstract():
    with pytest.raises(TypeError):
        KnowledgeProvider()