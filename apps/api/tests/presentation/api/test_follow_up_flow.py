from fastapi.testclient import TestClient

from app.application.factories.conversation_orchestrator_factory import (
    create_conversation_orchestrator,
)
from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.fakes.fake_knowledge_provider import (
    FakeKnowledgeProvider,
)
from app.application.fakes.fake_language_model import FakeLanguageModel
from app.application.use_cases.send_message import SendMessageUseCase
from app.application.use_cases.start_follow_up import StartFollowUpUseCase
from app.main import app
from app.presentation.api.dependencies import (
    get_send_message_use_case,
    get_start_follow_up_use_case,
)


def test_follow_up_flow_starts_and_processes_message() -> None:
    repository = FakeConversationRepository()
    knowledge_provider = FakeKnowledgeProvider()
    language_model = FakeLanguageModel()

    orchestrator = create_conversation_orchestrator(
        knowledge_provider=knowledge_provider,
        language_model=language_model,
    )

    start_follow_up_use_case = StartFollowUpUseCase(
        repository=repository,
    )

    send_message_use_case = SendMessageUseCase(
        repository=repository,
        orchestrator=orchestrator,
    )

    app.dependency_overrides[
        get_start_follow_up_use_case
    ] = lambda: start_follow_up_use_case

    app.dependency_overrides[
        get_send_message_use_case
    ] = lambda: send_message_use_case

    try:
        client = TestClient(app)

        start_response = client.post(
            "/follow-up/start",
            json={
                "patient_id": "patient-001",
            },
        )

        assert start_response.status_code == 200
        assert start_response.json() == {
            "conversation_id": "patient-001",
            "current_state": "greeting",
        }

        message_response = client.post(
            "/messages",
            json={
                "conversation_id": "patient-001",
                "message": "Tengo fiebre desde ayer.",
            },
        )

        assert message_response.status_code == 200

        body = message_response.json()

        assert body["response"] == "Respuesta clínica simulada."
        assert body["current_state"] == "patient_verification"

        assert knowledge_provider.last_query is not None

        assert language_model.last_prompt is not None
        assert "Tengo fiebre desde ayer." in language_model.last_prompt
        assert "clinical-guide" in language_model.last_prompt
        assert "chunk-001" in language_model.last_prompt

    finally:
        app.dependency_overrides.clear()
