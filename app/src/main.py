"""
Cloud-Native CI/CD Platform — Sample Application

A deliberately small FastAPI app. Its job is to give the pipeline something
real to build, test, scan, and deploy — the DevOps automation is the point
of this project, not the app itself.
"""

from datetime import datetime, timezone
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Cloud-Native CI/CD Platform - Sample App",
    version="1.0.0",
)


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


# In-memory store — intentionally simple, this app exists to be deployed,
# not to be a production task manager.
_tasks: Dict[int, Task] = {
    1: Task(id=1, title="Set up CI pipeline", done=True),
    2: Task(id=2, title="Deploy to EC2", done=False),
}


@app.get("/")
def root():
    return {"message": "Cloud-Native CI/CD Platform is running"}


@app.get("/health")
def health():
    """
    Used by health-check.sh and by the CD pipeline to verify a deploy
    actually succeeded before marking it as done.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/tasks")
def list_tasks():
    return list(_tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = _tasks.get(task_id)
    if task is None:
        return {"error": "task not found"}
    return task


@app.post("/tasks")
def create_task(task: Task):
    _tasks[task.id] = task
    return task
