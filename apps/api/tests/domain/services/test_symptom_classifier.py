from app.domain.services.symptom_classifier import (
    SymptomClassifier,
)


def test_detects_high_risk_symptom():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "fiebre",
            "dolor intenso",
        ]
    )

    assert result == "high"


def test_detects_medium_risk_symptom():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "dolor",
        ]
    )

    assert result == "medium"


def test_detects_low_risk_symptom():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "picazón",
        ]
    )

    assert result == "low"


def test_unknown_symptom_defaults_to_low():
    classifier = SymptomClassifier()

    result = classifier.classify(
        [
            "síntoma desconocido",
        ]
    )

    assert result == "low"