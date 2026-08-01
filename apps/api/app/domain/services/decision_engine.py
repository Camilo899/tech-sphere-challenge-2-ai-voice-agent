from app.domain.entities.conversation_context import (
    ConversationContext,
)
from app.domain.services.symptom_classifier import (
    SymptomClassifier,
)
from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.risk_level import (
    RiskLevel,
)


class DecisionEngine:
    """
    Determines the appropriate clinical decision
    based on the patient's conversation context.
    """

    def __init__(
        self,
        classifier: SymptomClassifier | None = None,
    ) -> None:
        self._classifier = (
            classifier
            if classifier is not None
            else SymptomClassifier()
        )

    def decide(
        self,
        risk_level: RiskLevel,
    ) -> ClinicalDecision:
        if risk_level is RiskLevel.HIGH:
            return ClinicalDecision.ESCALATE

        if risk_level is RiskLevel.MEDIUM:
            return ClinicalDecision.ASK_MORE

        return ClinicalDecision.CONTINUE

    def decide_from_context(
        self,
        context: ConversationContext,
    ) -> ClinicalDecision:
        risk_level = self._classifier.classify(
            context.symptoms,
        )

        return self.decide(risk_level)