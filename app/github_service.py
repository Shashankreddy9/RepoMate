import os

from dotenv import load_dotenv
from github import Github
from github.GithubException import GithubException


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_github_client():
    """
    Create an authenticated GitHub client.
    """

    if not GITHUB_TOKEN:
        return Github()

    return Github(GITHUB_TOKEN)


def get_repository(repo_url: str):
    """
    Fetch repository information from GitHub.
    """

    try:
        repo_path = repo_url.rstrip("/").split("github.com/")[-1]

        github = get_github_client()
        repository = github.get_repo(repo_path)

        return {
            "name": repository.name,
            "full_name": repository.full_name,
            "description": repository.description,
            "stars": repository.stargazers_count,
            "forks": repository.forks_count,
            "language": repository.language,
            "url": repository.html_url,
        }

    except GithubException as error:
        return {
            "error": f"GitHub API error: {error}"
        }

    except Exception as error:
        return {
            "error": f"Unexpected error: {error}"
        }