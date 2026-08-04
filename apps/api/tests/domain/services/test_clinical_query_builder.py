from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.clinical_query_builder import (
    ClinicalQueryBuilder,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.conversation_state import (
    ConversationState,
)


def test_build_query_from_symptoms():
    context = ConversationContext(
        conversation_id="conv-001",
        current_state=ConversationState.GREETING,
        clinical_decision=ClinicalDecision.CONTINUE,
    )

    context.symptoms.extend(
        [
            "fiebre",
            "dolor",
            "enrojecimiento",
        ]
    )

    builder = ClinicalQueryBuilder()

    query = builder.build(context)

    assert query == (
        "fiebre dolor enrojecimiento"
    )