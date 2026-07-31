from typing import ClassVar

from app.domain.value_objects.risk_level import (
    RiskLevel,
)


class SymptomClassifier:
    """
    Classifies symptoms according to their
    clinical risk level.
    """

    _HIGH_RISK: ClassVar[set[str]] = {
        "fiebre",
        "sangrado",
        "dificultad para respirar",
        "dolor intenso",
    }

    _MEDIUM_RISK: ClassVar[set[str]] = {
        "dolor",
        "inflamación",
        "enrojecimiento",
    }

    def classify(
        self,
        symptoms: list[str],
    ) -> RiskLevel:
        normalized = {
            symptom.strip().lower()
            for symptom in symptoms
        }

        if normalized & self._HIGH_RISK:
            return RiskLevel.HIGH

        if normalized & self._MEDIUM_RISK:
            return RiskLevel.MEDIUM

        return RiskLevel.LOW