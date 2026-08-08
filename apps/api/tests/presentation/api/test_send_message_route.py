from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_send_message_route() -> None:
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

    assert body["current_state"] == (
        "patient_verification"
    )
