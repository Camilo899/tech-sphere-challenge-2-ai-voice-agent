from enum import Enum


class RiskLevel(str, Enum):
    """
    Represents the clinical risk level determined
    during a postoperative follow-up.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"