from app.scanners.gitleaks_runner import run_gitleaks

def handle_pr(repo_path):
    results = run_gitleaks(repo_path)
    return results