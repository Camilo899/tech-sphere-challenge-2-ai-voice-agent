from app.domain.value_objects.risk_level import (
    RiskLevel,
)


def test_risk_level_values():
    assert RiskLevel.LOW.value == "low"
    assert RiskLevel.MEDIUM.value == "medium"
    assert RiskLevel.HIGH.value == "high"