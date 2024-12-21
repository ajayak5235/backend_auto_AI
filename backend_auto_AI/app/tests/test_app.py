from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_pr():
    response = client.post("/analyze-pr", json={})
    assert response.status_code == 200
    assert "task_id" in response.json()

def test_status():
    response = client.get("/status/sample_task_id")
    assert response.status_code == 200
    assert "status" in response.json()