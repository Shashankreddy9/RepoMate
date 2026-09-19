from app.github_service import get_github_client


def get_repository_files(repo_url: str):
    """
    Recursively fetch files from a GitHub repository.
    """

    repo_path = repo_url.rstrip("/").split("github.com/")[-1]

    github = get_github_client()
    repository = github.get_repo(repo_path)

    files = []

    def collect_files(contents):

        for item in contents:

            if item.type == "file":

                files.append(
                    {
                        "name": item.name,
                        "path": item.path,
                        "download_url": item.download_url,
                    }
                )

            elif item.type == "dir":

                directory_contents = repository.get_contents(
                    item.path
                )

                collect_files(directory_contents)

    root_contents = repository.get_contents("")

    collect_files(root_contents)

    return files