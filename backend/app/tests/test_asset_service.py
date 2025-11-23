from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_assets():
    resp = client.get("/api/v1/assets")
    assert resp.status_code == 200
    data = resp.json()
    assert "assets" in data
    assert isinstance(data["assets"], list)


