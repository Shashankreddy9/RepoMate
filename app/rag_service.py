from app.search_service import (
    build_repository_index,
    search_repository,
)


def build_rag_context(
    repo_url: str,
    question: str,
    top_k: int = 3,
):
    """
    Build context from the most relevant repository code.
    """

    vector_store = build_repository_index(
        repo_url
    )

    results = search_repository(
        vector_store,
        question,
        top_k,
    )

    context_parts = []

    for result in results:

        document = result["document"]

        context_parts.append(
            f"File: {document['path']}\n"
            f"Code:\n{document['content']}"
        )

    return "\n\n---\n\n".join(
        context_parts
    )