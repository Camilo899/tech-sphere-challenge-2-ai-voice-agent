from enum import StrEnum


class ClinicalDecision(StrEnum):
    CONTINUE = "continue"

    ASK_MORE = "ask_more"

    ESCALATE = "escalate"

    UNKNOWN = "unknown"