from typing import ClassVar


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
    ) -> str:
        normalized = {
            symptom.strip().lower()
            for symptom in symptoms
        }

        if normalized & self._HIGH_RISK:
            return "high"

        if normalized & self._MEDIUM_RISK:
            return "medium"

        return "low"