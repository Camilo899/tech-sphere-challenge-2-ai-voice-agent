from uuid import uuid4

from app.domain.entities.follow_up_case import FollowUpCase
from app.domain.value_objects.risk_level import RiskLevel


def test_follow_up_case_starts_with_low_risk():
    patient_id = uuid4()

    case = FollowUpCase.create(patient_id)

    assert case.patient_id == patient_id
    assert case.risk_level == RiskLevel.LOW