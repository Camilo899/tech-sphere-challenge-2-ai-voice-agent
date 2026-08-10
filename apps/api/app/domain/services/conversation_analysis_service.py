from app.domain.services.symptom_classifier import SymptomClassifier
from app.domain.value_objects.risk_level import RiskLevel


class ConversationAnalysisService:
    """
    Extracts relevant symptoms from a patient message
    and determines the corresponding risk level.
    """

    def __init__(
        self,
        symptom_classifier: SymptomClassifier | None = None,
    ) -> None:
        self._symptom_classifier = (
            symptom_classifier
            if symptom_classifier is not None
            else SymptomClassifier()
        )

    def extract_symptoms(
        self,
        message: str,
    ) -> list[str]:
        normalized_message = message.strip().lower()

        known_symptoms = (
            self._symptom_classifier.high_risk_symptoms
            | self._symptom_classifier.medium_risk_symptoms
        )

        return [
            symptom
            for symptom in known_symptoms
            if symptom in normalized_message
        ]

    def assess_risk(
        self,
        symptoms: list[str],
    ) -> RiskLevel:
        return self._symptom_classifier.classify(symptoms)
