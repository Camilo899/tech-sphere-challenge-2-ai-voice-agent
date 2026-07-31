from app.domain.services.decision_engine import (
    DecisionEngine,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.risk_level import (
    RiskLevel,
)


def test_high_risk_requires_escalation():
    engine = DecisionEngine()

    decision = engine.decide(
        RiskLevel.HIGH,
    )

    assert decision is ClinicalDecision.ESCALATE


def test_medium_risk_requires_more_questions():
    engine = DecisionEngine()

    decision = engine.decide(
        RiskLevel.MEDIUM,
    )

    assert decision is ClinicalDecision.ASK_MORE


def test_low_risk_can_continue():
    engine = DecisionEngine()

    decision = engine.decide(
        RiskLevel.LOW,
    )

    assert decision is ClinicalDecision.CONTINUE