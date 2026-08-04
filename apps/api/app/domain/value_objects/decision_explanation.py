from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionExplanation:
    """
    Explains why a clinical decision
    was made.
    """

    decision: str

    reason: str