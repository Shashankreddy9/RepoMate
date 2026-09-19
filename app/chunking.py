def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200):
    """
    Split text into overlapping chunks.
    """

    if not text:
        return []

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_documents(documents):
    """
    Split repository documents into smaller chunks.
    """

    chunks = []

    for document in documents:

        text_chunks = chunk_text(
            document["content"]
        )

        for index, text in enumerate(text_chunks):

            chunks.append(
                {
                    "path": document["path"],
                    "chunk_id": index,
                    "content": text,
                }
            )

    return chunks