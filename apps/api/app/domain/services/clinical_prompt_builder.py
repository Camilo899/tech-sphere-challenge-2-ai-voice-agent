from app.domain.value_objects.evidence import Evidence


class ClinicalPromptBuilder:
    """
    Builds a structured prompt from a patient message
    and retrieved clinical evidence.
    """

    def build(
        self,
        *,
        patient_message: str,
        evidence: list[Evidence],
    ) -> str:
        evidence_text = "\n".join(
            (
                f"- Documento: {item.document_name}; "
                f"sección: {item.section}; "
                f"fragmento: {item.chunk_id}; "
                f"relevancia: {item.score:.3f}"
            )
            for item in evidence
        )

        return (
            "You are a clinical assistant supporting "
            "postoperative follow-up.\n\n"
            "Patient message:\n"
            f"{patient_message}\n\n"
            "Retrieved clinical evidence:\n"
            f"{evidence_text}\n\n"
            "Use only the retrieved evidence when providing "
            "clinical guidance."
        )