from app.presentation.schemas.start_follow_up_request_schema import (
    StartFollowUpRequestSchema,
)


def test_request_schema():
    schema = StartFollowUpRequestSchema(
        patient_id="patient-001",
    )

    assert schema.patient_id == "patient-001"