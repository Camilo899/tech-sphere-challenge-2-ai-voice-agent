"""
Follow-up lifecycle states.

This module defines the valid states of a postoperative follow-up case.
"""

from enum import StrEnum


class FollowUpStatus(StrEnum):
    """Represents the lifecycle of a follow-up case."""

    CREATED = "created"
    IN_PROGRESS = "in_progress"
    WAITING_INFORMATION = "waiting_information"
    READY_FOR_DECISION = "ready_for_decision"
    ESCALATED = "escalated"
    COMPLETED = "completed"