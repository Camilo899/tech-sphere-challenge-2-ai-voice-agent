from enum import Enum


class ConversationState(str, Enum):
    GREETING = "greeting"

    PATIENT_VERIFICATION = "patient_verification"

    SYMPTOM_COLLECTION = "symptom_collection"

    CLARIFICATION = "clarification"

    KNOWLEDGE_RETRIEVAL = "knowledge_retrieval"

    CLINICAL_REASONING = "clinical_reasoning"

    DECISION = "decision"

    SUMMARY = "summary"

    FINISHED = "finished"