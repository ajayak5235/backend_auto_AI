from fastapi import FastAPI, BackgroundTasks
from celery.result import AsyncResult
from .worker import analyze_pr_task
from .schemas import AnalyzePRRequest, AnalyzePRResponse, TaskStatusResponse
from .db import get_task_result

app = FastAPI()

@app.post("/analyze-pr", response_model=AnalyzePRResponse)
def analyze_pr(request: AnalyzePRRequest, background_tasks: BackgroundTasks):
    task = analyze_pr_task.delay(request.repo_url, request.pr_number, request.github_token)
    return {"task_id": task.id}

@app.get("/status/{task_id}", response_model=TaskStatusResponse)
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status}

@app.get("/results/{task_id}")
def get_results(task_id: str):
    result = get_task_result(task_id)
    if not result:
        return {"message": "Task result not found"}
    return result