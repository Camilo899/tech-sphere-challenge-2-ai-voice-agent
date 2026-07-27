from app.domain.value_objects.risk_level import RiskLevel


def test_should_have_four_risk_levels():
    assert len(RiskLevel) == 4


def test_default_low_value():
    assert RiskLevel.LOW == "low"


def test_critical_value():
    assert RiskLevel.CRITICAL == "critical"