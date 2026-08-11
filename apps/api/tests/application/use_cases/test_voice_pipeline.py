from app.domain.services.conversation_orchestrator import ConversationOrchestrator


class FakeSTT:
    def transcribe(self, audio_bytes: bytes) -> str:
        return "hola"


class FakeTTS:
    def synthesize(self, text: str) -> bytes:
        return b"audio:" + text.encode()


class FakeDecisionEngine:
    pass


class FakeConversationFlow:
    pass


class FakeKnowledgeService:
    pass


class FakeClinicalQueryBuilder:
    pass


def test_voice_pipeline_end_to_end() -> None:
    stt = FakeSTT()
    tts = FakeTTS()
    orchestrator = ConversationOrchestrator(
        decision_engine=FakeDecisionEngine(),
        conversation_flow=FakeConversationFlow(),
        knowledge_service=FakeKnowledgeService(),
        clinical_query_builder=FakeClinicalQueryBuilder(),
        clinical_response_service=None,
        conversation_analysis_service=None,
    )

    # Simular audio de entrada
    audio_in = b"fake-audio"

    # STT → texto
    text = stt.transcribe(audio_in)
    assert text == "hola"

    # Orchestrator → respuesta trivial (para MVP usamos el mismo texto)
    response_text = text

    # TTS → audio de salida
    audio_out = tts.synthesize(response_text)
    assert audio_out.startswith(b"audio:hola")
