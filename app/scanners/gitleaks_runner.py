import subprocess
import json

def run_gitleaks(repo_path):
    result = subprocess.run(
        ["gitleaks", "detect", "--source", repo_path, "--report-format", "json"],
        capture_output=True,
        text=True
    )

    try:
        return json.loads(result.stdout)
    except:
        return []