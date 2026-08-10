from app.domain.services.conversation_analysis_service import (
    ConversationAnalysisService,
)
from app.domain.value_objects.risk_level import RiskLevel


def test_extracts_high_risk_symptom_from_patient_message() -> None:
    service = ConversationAnalysisService()

    symptoms = service.extract_symptoms(
        "Tengo fiebre desde ayer después de la cirugía.",
    )

    assert "fiebre" in symptoms


def test_assesses_high_risk_from_extracted_symptom() -> None:
    service = ConversationAnalysisService()

    risk = service.assess_risk(
        ["fiebre"],
    )

    assert risk is RiskLevel.HIGH


def test_extracts_medium_risk_symptom_from_patient_message() -> None:
    service = ConversationAnalysisService()

    symptoms = service.extract_symptoms(
        "Tengo inflamación en la zona de la cirugía.",
    )

    assert "inflamación" in symptoms
