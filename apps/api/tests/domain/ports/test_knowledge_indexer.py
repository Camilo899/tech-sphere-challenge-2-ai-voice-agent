import pytest

from app.domain.ports.knowledge_indexer import KnowledgeIndexer


def test_knowledge_indexer_is_abstract():
    with pytest.raises(TypeError):
        KnowledgeIndexer()
