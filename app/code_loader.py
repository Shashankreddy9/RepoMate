from app.repository_service import get_repository_files
from app.file_service import get_file_content


SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".html",
    ".css",
    ".md",
    ".txt",
}


def load_repository_code(repo_url: str):
    """
    Load supported text files from a GitHub repository.
    """

    files = get_repository_files(repo_url)

    documents = []

    for file in files:

        path = file["path"]

        if not any(
            path.lower().endswith(extension)
            for extension in SUPPORTED_EXTENSIONS
        ):
            continue

        try:

            content = get_file_content(
                repo_url,
                path,
            )

            documents.append(
                {
                    "path": path,
                    "content": content,
                }
            )

        except Exception:
            continue

    return documents