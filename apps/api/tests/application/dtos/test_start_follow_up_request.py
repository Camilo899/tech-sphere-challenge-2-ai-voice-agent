from app.application.dtos.start_follow_up_request import (
    StartFollowUpRequest,
)


def test_start_follow_up_request():
    request = StartFollowUpRequest(
        patient_id="patient-001",
    )

    assert request.patient_id == "patient-001"