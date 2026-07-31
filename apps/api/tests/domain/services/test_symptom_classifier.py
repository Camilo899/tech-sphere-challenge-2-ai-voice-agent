from app.domain.services.symptom_classifier import (
    SymptomClassifier,
)
from app.domain.value_objects.risk_level import (
    RiskLevel,
)


def test_detects_high_risk_symptom():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "fiebre",
            "dolor intenso",
        ]
    )

    assert result is RiskLevel.HIGH


def test_detects_medium_risk_symptom():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "dolor",
        ]
    )

    assert result is RiskLevel.MEDIUM


def test_detects_low_risk_symptom():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "picazón",
        ]
    )

    assert result is RiskLevel.LOW


def test_unknown_symptom_defaults_to_low():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "síntoma desconocido",
        ]
    )

    assert result is RiskLevel.LOW