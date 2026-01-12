from typing import List
import math

from sentence_transformers import SentenceTransformer
from app.core.config import settings


_model = SentenceTransformer(settings.embedding_model)


def normalize_text(text: str) -> str:
    return text.strip()


def build_embedding(title: str, description: str) -> List[float]:

    text = f"{title}. {description}".strip()

    embedding = _model.encode(
        text,
        convert_to_numpy=True,       
        normalize_embeddings=True    
    ).tolist()

    if len(embedding) != settings.typesense_vector_dim:
        raise ValueError(f"Invalid embedding size: {len(embedding)}")

    if any(math.isnan(x) or math.isinf(x) for x in embedding):
        raise ValueError("Embedding contains NaN or Inf")

    if all(x == 0.0 for x in embedding):
        raise ValueError("Zero embedding detected")

    return [float(x) for x in embedding]