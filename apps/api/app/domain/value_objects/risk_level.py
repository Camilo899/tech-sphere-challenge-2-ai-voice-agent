from enum import StrEnum


class RiskLevel(StrEnum):
    """
    Clinical risk level assigned to a postoperative follow-up.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"