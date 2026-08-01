from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.decision_engine import (
    DecisionEngine,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.conversation_state import (
    ConversationState,
)


def test_decision_engine_uses_context_symptoms():
    engine = DecisionEngine()

    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    context.symptoms.extend(
        [
            "fiebre",
        ]
    )

    decision = engine.decide_from_context(
        context,
    )

    assert decision is ClinicalDecision.ESCALATE