from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_start_follow_up_endpoint():
    response = client.post(
        "/follow-up/start",
        json={
            "patient_id": "patient-001",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "conversation_id" in body

    assert body["current_state"] == "greeting"