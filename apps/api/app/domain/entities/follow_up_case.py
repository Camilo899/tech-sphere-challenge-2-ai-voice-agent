from dataclasses import dataclass
from uuid import UUID, uuid4

from app.domain.value_objects.risk_level import RiskLevel


@dataclass
class FollowUpCase:
    """
    Represents a postoperative follow-up case.
    """

    id: UUID
    patient_id: UUID
    risk_level: RiskLevel

    @classmethod
    def create(cls, patient_id: UUID) -> "FollowUpCase":
        return cls(
            id=uuid4(),
            patient_id=patient_id,
            risk_level=RiskLevel.LOW,
        )