from celery import Celery
from .utils import analyze_code

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task(bind=True)
def analyze_pr_task(self, repo_url, pr_number, github_token=None):
    try:
        return analyze_code(repo_url, pr_number, github_token)
    except Exception as e:
        self.update_state(state="FAILURE", meta={"exc": str(e)})
        raise e