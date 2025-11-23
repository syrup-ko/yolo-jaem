from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_simulate():
    resp = client.post(
        "/api/v1/simulate",
        json={
            "assets": ["Stock", "HYSA"],
            "durationYears": 1,
            "initialCapital": 1000000,
            "monthlyContribution": 100000,
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "timeline" in data and "assets" in data
    assert len(data["assets"]) == 2


