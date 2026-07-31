from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_returns_message():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check_returns_healthy_status():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert "timestamp" in body


def test_list_tasks_returns_seeded_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2


def test_get_task_by_id():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Set up CI pipeline"


def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 200
    assert response.json() == {"error": "task not found"}


def test_create_task():
    new_task = {"id": 3, "title": "Write README", "done": False}
    response = client.post("/tasks", json=new_task)
    assert response.status_code == 200
    assert response.json()["title"] == "Write README"

    # Confirm it was actually stored
    get_response = client.get("/tasks/3")
    assert get_response.json()["title"] == "Write README"
