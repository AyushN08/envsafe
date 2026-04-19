from fastapi import APIRouter, Request
from app.core.orchestrator import handle_pr

router = APIRouter()

@router.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    event = request.headers.get("X-GitHub-Event")

    print(f"Received event: {event}")

    # Only handle pull request events
    if event == "pull_request":
        action = payload.get("action")
        print(f"PR action: {action}")

        # Only act on opened/synchronized PRs
        if action in ["opened", "synchronize"]:
            print("Running scan pipeline...")

            # For now, use local test repo path
            repo_path = "./test_repo"   # 👈 create this folder for testing

            results = handle_pr(repo_path)

            print("Scan results:", results)

    return {"status": "ok"}