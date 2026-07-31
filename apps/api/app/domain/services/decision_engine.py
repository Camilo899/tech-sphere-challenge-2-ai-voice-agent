from typing import ClassVar

from app.domain.value_objects.clinical_decision import (
    ClinicalDecision,
)
from app.domain.value_objects.risk_level import (
    RiskLevel,
)


class DecisionEngine:
    """
    Determines the clinical decision based
    on the assessed risk level.
    """

    _DECISIONS: ClassVar[
        dict[RiskLevel, ClinicalDecision]
    ] = {
        RiskLevel.LOW:
            ClinicalDecision.CONTINUE,

        RiskLevel.MEDIUM:
            ClinicalDecision.ASK_MORE,

        RiskLevel.HIGH:
            ClinicalDecision.ESCALATE,
    }

    def decide(
        self,
        risk_level: RiskLevel,
    ) -> ClinicalDecision:
        return self._DECISIONS[risk_level]