from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_global_exception_handler():
    response = client.get("/health/error")

    assert response.status_code == 500

    assert response.json() == {
        "error": "Internal Server Error",
        "detail": "Test exception",
    }