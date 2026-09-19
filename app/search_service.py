from app.code_loader import load_repository_code
from app.chunking import chunk_documents
from app.embeddings import generate_embeddings
from app.vector_store import VectorStore


def build_repository_index(repo_url: str):
    """
    Build a searchable vector index for a GitHub repository.
    """

    documents = load_repository_code(repo_url)

    chunks = chunk_documents(documents)

    if not chunks:
        raise ValueError(
            "No supported source files found."
        )

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = generate_embeddings(texts)

    vector_store = VectorStore(
        dimension=len(embeddings[0])
    )

    vector_store.add(
        embeddings,
        chunks,
    )

    return vector_store


def search_repository(
    vector_store,
    query: str,
    top_k: int = 3,
):
    """
    Search the repository for relevant code chunks.
    """

    query_embedding = generate_embeddings(
        [query]
    )[0]

    return vector_store.search(
        query_embedding,
        top_k,
    )