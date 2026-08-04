from app.domain.entities.conversation_context import (
    ConversationContext,
)


class ClinicalQueryBuilder:
    """
    Builds a clinical query from the
    current conversation context.
    """

    def build(
        self,
        context: ConversationContext,
    ) -> str:
        """
        Creates a search query based on
        collected symptoms.
        """
        return " ".join(context.symptoms)