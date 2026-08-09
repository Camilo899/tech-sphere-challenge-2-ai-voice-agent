from fastapi.testclient import TestClient

from app.application.fakes.fake_language_model import (
    FakeLanguageModel,
)
from app.application.fakes.fake_conversation_repository import (
    FakeConversationRepository,
)
from app.application.factories.conversation_orchestrator_factory import (
    create_conversation_orchestrator,
)
from app.application.use_cases.send_message import (
    SendMessageUseCase,
)
from app.main import app
from app.presentation.api.dependencies import (
    get_send_message_use_case,
    get_start_follow_up_use_case,
)


def test_send_message_route() -> None:
    repository = FakeConversationRepository()

    start_use_case = __import__(
        "app.application.use_cases.start_follow_up",
        fromlist=["StartFollowUpUseCase"],
    ).StartFollowUpUseCase(repository)

    orchestrator = create_conversation_orchestrator(
        language_model=FakeLanguageModel(),
    )

    send_use_case = SendMessageUseCase(
        repository=repository,
        orchestrator=orchestrator,
    )

    app.dependency_overrides[
        get_start_follow_up_use_case
    ] = lambda: start_use_case

    app.dependency_overrides[
        get_send_message_use_case
    ] = lambda: send_use_case

    client = TestClient(app)

    try:
        start_response = client.post(
            "/follow-up/start",
            json={
                "patient_id": "patient-001",
            },
        )

        assert start_response.status_code == 200

        conversation_id = start_response.json()[
            "conversation_id"
        ]

        response = client.post(
            "/messages",
            json={
                "conversation_id": conversation_id,
                "message": "Tengo fiebre desde ayer.",
            },
        )

        assert response.status_code == 200

        body = response.json()

        assert "response" in body
        assert "current_state" in body

        assert body["response"] == (
            "Respuesta clínica simulada."
        )

        assert body["current_state"] == (
            "patient_verification"
        )
    finally:
        app.dependency_overrides.clear()
