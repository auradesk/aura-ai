from sentence_transformers import SentenceTransformer
import numpy as np

# Load lightweight model
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str):

    embedding = model.encode(text)

    return embedding


def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot = np.dot(vec1, vec2)

    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    similarity = dot / (norm1 * norm2)

    return similarity
