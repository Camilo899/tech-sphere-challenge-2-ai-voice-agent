from app.domain.value_objects.decision_explanation import (
    DecisionExplanation,
)


def test_decision_explanation():
    explanation = DecisionExplanation(
        decision="ESCALATE",
        reason="Patient reports fever.",
    )

    assert explanation.decision == "ESCALATE"

    assert explanation.reason == (
        "Patient reports fever."
    )