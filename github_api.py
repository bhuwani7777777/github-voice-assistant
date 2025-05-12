import requests
from config import GITHUB_TOKEN

headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def get_issues(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        issues = response.json()
        return [f"Issue: {issue['title']}" for issue in issues]
    else:
        return ["❌ Failed to fetch issues."]
