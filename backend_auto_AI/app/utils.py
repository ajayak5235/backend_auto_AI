import requests
# from .ai.ollama_ai import analyze_diff_with_ollama
from .ai.openai_api import analyze_diff_with_openai

def fetch_diff(repo_url, pr_number, github_token=None):
    headers = {"Authorization": f"token {github_token}"} if github_token else {}
    response = requests.get(f"{repo_url}/pull/{pr_number}/files", headers=headers)
    response.raise_for_status()
    return response.text



def analyze_code(repo_url, pr_number, github_token=None):
    diff = fetch_diff(repo_url, pr_number, github_token)
    try:
        ai_results = analyze_diff_with_openai(diff)

        # Transform AI results into the expected structure
        results = {
            "files": ai_results["files"],  # Assume the AI response includes analyzed files and issues
            "summary": {
                "total_files": len(ai_results["files"]),
                "total_issues": sum(len(file["issues"]) for file in ai_results["files"]),
                "critical_issues": sum(
                    1 for file in ai_results["files"] for issue in file["issues"] if issue.get("type") == "critical"
                ),
            },
        }
        return results
    except Exception as e:
        raise RuntimeError(f"AI analysis failed: {e}")
