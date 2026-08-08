from abc import ABC, abstractmethod
from app.domain.value_objects.llm_response import LLMResponse


class LanguageModel(ABC):
    """
    Port for generating responses from a language model.
    """

    @abstractmethod
    def generate(
        self,
        *,
        prompt: str,
    ) -> LLMResponse:
        """
        Generates a response for the given prompt.
        """