from dataclasses import dataclass


@dataclass(frozen=True)
class LanguageModelResponse:
    """
    Represents the structured interpretation generated
    by the language model for a conversation turn.
    """

    response: str
    symptoms: list[str]
    uncertainty: bool
