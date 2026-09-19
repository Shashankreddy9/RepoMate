from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embeddings(texts):
    """
    Convert text into numerical embeddings.
    """

    if not texts:
        return []

    embeddings = model.encode(
        texts,
        show_progress_bar=False,
    )

    return embeddings