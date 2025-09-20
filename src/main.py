from typing import List

def split_into_chunks(doc_file: str) -> List[str]:
    """
    Splits the content of a document into chunks based on double newlines.
    :param doc_file: The path to the document file.
    :return: A list of chunks.
    """
    with open(doc_file, 'r', encoding='utf-8') as file:
        content = file.read()

    return [chunk for chunk in content.split("\n\n")]


chunks = split_into_chunks(".\src\doc.md")

for i, chunk in enumerate(chunks):
    print(f"[{i}] {chunk}\n")


# from sentence_transformers import SentenceTransformer

# embedding_model = SentenceTransformer("shibing624/text2vec-base-chinese")

# def embed_chunk(chunk: str) -> List[float]:
#     embedding = embedding_model.encode(chunk, normalize_embeddings=True)
#     return embedding.tolist()


# embedding = embed_chunk("测试内容")
# print(len(embedding))
# print(embedding)