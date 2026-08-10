from datetime import UTC, datetime

from app.application.factories.conversation_orchestrator_factory import (
    create_conversation_orchestrator,
)
from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)
from app.application.fakes.fake_language_model import FakeLanguageModel
from app.domain.entities.conversation_context import ConversationContext
from app.domain.value_objects.clinical_decision import ClinicalDecision
from app.domain.value_objects.conversation_message import ConversationMessage
from app.domain.value_objects.conversation_state import ConversationState


def test_orchestrator_processes_message() -> None:
    language_model = FakeLanguageModel()

    knowledge_provider = FakeKnowledgeProvider()

    orchestrator = create_conversation_orchestrator(
        knowledge_provider=knowledge_provider,
        language_model=language_model,
)

    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    context.symptoms.append("fiebre")

    message = ConversationMessage(
        speaker="patient",
        content="Tengo fiebre desde ayer.",
        timestamp=datetime.now(UTC),
    )

    updated = orchestrator.process(
        context=context,
        message=message,
    )

    assert len(updated.messages) == 2

    assert updated.messages[0] is message

    assert updated.messages[1].speaker == "assistant"

    assert (
        updated.messages[1].content
        == "Respuesta clínica simulada."
    )

    assert (
        updated.clinical_decision
        is ClinicalDecision.ESCALATE
    )

    assert (
        updated.current_state
        is ConversationState.PATIENT_VERIFICATION
    )

    assert len(updated.evidences) == 1

    assert updated.evidences[0].chunk_id == "chunk-001"
    
    assert knowledge_provider.last_query == "fiebre"
    
    assert "Tengo fiebre desde ayer." in language_model.last_prompt

def test_orchestrator_escalates_high_risk_symptom() -> None:
    language_model = FakeLanguageModel()
    knowledge_provider = FakeKnowledgeProvider()

    orchestrator = create_conversation_orchestrator(
        knowledge_provider=knowledge_provider,
        language_model=language_model,
    )

    context = ConversationContext(
        conversation_id="conv-high-risk",
        current_state=ConversationState.SYMPTOM_COLLECTION,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    message = ConversationMessage(
        speaker="patient",
        content="Tengo fiebre desde ayer después de la cirugía.",
        timestamp=datetime.now(UTC),
    )

    updated = orchestrator.process(
        context=context,
        message=message,
    )

    assert "fiebre" in updated.symptoms

    assert (
        updated.clinical_decision
        is ClinicalDecision.ESCALATE
    )