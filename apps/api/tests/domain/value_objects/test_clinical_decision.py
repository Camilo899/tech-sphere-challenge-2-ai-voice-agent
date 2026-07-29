from app.domain.value_objects.clinical_decision import ClinicalDecision


def test_clinical_decisions_are_defined():
    assert ClinicalDecision.CONTINUE.value == "continue"
    assert ClinicalDecision.ASK_MORE.value == "ask_more"
    assert ClinicalDecision.ESCALATE.value == "escalate"
    assert ClinicalDecision.UNKNOWN.value == "unknown"