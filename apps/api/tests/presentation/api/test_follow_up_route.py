from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_start_follow_up_endpoint():
    response = client.post("/follow-up/start")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok",
    }