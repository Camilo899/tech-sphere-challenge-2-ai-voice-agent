from app.domain.value_objects.follow_up_status import FollowUpStatus


def test_should_define_all_follow_up_statuses() -> None:
    """The follow-up workflow must expose six valid statuses."""

    assert len(FollowUpStatus) == 6


def test_should_have_created_as_initial_status() -> None:
    """The initial status should be CREATED."""

    assert FollowUpStatus.CREATED.value == "created"


def test_should_have_completed_status() -> None:
    """The workflow should expose a completed status."""

    assert FollowUpStatus.COMPLETED.value == "completed"