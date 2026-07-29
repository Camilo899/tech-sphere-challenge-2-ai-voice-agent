from enum import Enum


class ClinicalDecision(str, Enum):
    CONTINUE = "continue"

    ASK_MORE = "ask_more"

    ESCALATE = "escalate"

    UNKNOWN = "unknown"