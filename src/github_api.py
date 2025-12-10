import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com"

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# ---------------------------
# Helper: Split "owner/repo"
# ---------------------------
def split_repo(repo_string):
    """
    Takes 'owner/repo' and returns ('owner', 'repo')
    """
    if "/" not in repo_string:
        raise ValueError("Repository must be in format owner/repo")
    return repo_string.split("/")


# ---------------------------
# List repositories
# ---------------------------
def list_repositories(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


# ---------------------------
# Create issue
# ---------------------------
def create_issue(repo, title, body):
    url = f"{GITHUB_API_URL}/repos/{repo}/issues"
    issue_data = {"title": title, "body": body}
    response = requests.post(url, json=issue_data, headers=HEADERS)
    response.raise_for_status()
    return response.json()


# ---------------------------
# List issues
# ---------------------------
def list_issues(repo):
    url = f"{GITHUB_API_URL}/repos/{repo}/issues"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


# ---------------------------
# Close issue
# ---------------------------
def close_issue(repo, issue_number):
    url = f"{GITHUB_API_URL}/repos/{repo}/issues/{issue_number}"
    issue_data = {"state": "closed"}
    response = requests.patch(url, json=issue_data, headers=HEADERS)
    response.raise_for_status()
    return response.json()


# ---------------------------
# Add label to issue
# ---------------------------
def add_label(repo, issue_number, labels):
    url = f"{GITHUB_API_URL}/repos/{repo}/issues/{issue_number}/labels"
    payload = {"labels": labels}
    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()


# ---------------------------
# Auto-label based on keywords
# ---------------------------
def auto_label_issue(repo, issue_number, title, body=""):
    text = f"{title.lower()} {body.lower()}"

    keyword_to_label = {
        "bug": "bug",
        "error": "bug",
        "fix": "bug",
        "issue": "bug",
        "crash": "bug",

        "feature": "enhancement",
        "enhancement": "enhancement",
        "improve": "enhancement",
        "add": "enhancement",

        "docs": "documentation",
        "documentation": "documentation",

        "test": "tests",
        "testing": "tests"
    }

    labels = set()

    for keyword, label in keyword_to_label.items():
        if keyword in text:
            labels.add(label)

    if not labels:
        return {"message": "No labels matched"}

    return add_label(repo, issue_number, list(labels))
