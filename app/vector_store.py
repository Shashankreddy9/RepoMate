import faiss
import numpy as np


class VectorStore:
    """
    Store and search text embeddings using FAISS.
    """

    def __init__(self, dimension: int):
        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.documents = []

    def add(self, embeddings, documents):
        """
        Add embeddings and their documents to the vector store.
        """

        vectors = np.asarray(
            embeddings,
            dtype="float32",
        )

        self.index.add(vectors)

        self.documents.extend(documents)

    def search(self, query_embedding, top_k: int = 3):
        """
        Search for the most similar documents.
        """

        query_vector = np.asarray(
            [query_embedding],
            dtype="float32",
        )

        distances, indices = self.index.search(
            query_vector,
            top_k,
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0],
        ):

            if index == -1:
                continue

            results.append(
                {
                    "document": self.documents[index],
                    "distance": float(distance),
                }
            )

        return results