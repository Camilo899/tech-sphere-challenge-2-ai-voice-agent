from enum import StrEnum


class RiskLevel(StrEnum):
    """
    Clinical risk level assigned to a postoperative follow-up.
    associated with reported symptoms.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    #CRITICAL = "critical"