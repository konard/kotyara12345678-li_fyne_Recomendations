import os
from pydantic import BaseModel


class Settings(BaseModel):
    typesense_host: str = os.getenv("TYPESENSE_HOST", "localhost")
    typesense_port: int = int(os.getenv("TYPESENSE_PORT", "8108"))
    typesense_protocol: str = os.getenv("TYPESENSE_PROTOCOL", "http")
    typesense_api_key: str = os.getenv("TYPESENSE_API_KEY", "dev-key")
    typesense_collection: str = os.getenv("TYPESENSE_COLLECTION", "issues")
    typesense_vector_dim: int = int(os.getenv("TYPESENSE_VECTOR_DIM", "384"))
    forward_url: str = os.getenv("FORWARD_URL", "")
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )


settings = Settings()