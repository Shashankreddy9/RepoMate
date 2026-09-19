from app.github_service import get_github_client


def get_file_content(repo_url: str, file_path: str):
    """
    Fetch the content of a single file from GitHub.
    """

    repo_path = repo_url.rstrip("/").split("github.com/")[-1]

    github = get_github_client()
    repository = github.get_repo(repo_path)

    file = repository.get_contents(file_path)

    if isinstance(file, list):
        raise ValueError(
            "The provided path is a directory, not a file."
        )

    content = file.decoded_content.decode("utf-8")

    return content