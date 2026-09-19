from app.rag_service import build_rag_context
from app.llm_service import generate_answer


def answer_repository_question(
    repo_url: str,
    question: str,
    top_k: int = 3,
):
    """
    Answer a question about a GitHub repository
    using retrieved repository context.
    """

    context = build_rag_context(
        repo_url,
        question,
        top_k,
    )

    prompt = f"""
You are RepoMate, an AI assistant that helps developers
understand GitHub repositories.

Answer the user's question using ONLY the repository context
provided below.

If the context does not contain enough information to answer
the question, clearly say that the available repository
context is insufficient.

When possible, mention the relevant file paths.

Repository context:
--------------------
{context}
--------------------

User question:
{question}

Provide a clear and concise answer.
"""

    answer = generate_answer(prompt)

    return answer