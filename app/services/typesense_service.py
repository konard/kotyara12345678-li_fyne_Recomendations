from typing import List, Dict, Any, Optional
import typesense
from typesense.exceptions import ObjectNotFound
import httpx
import json

from app.core.config import settings
from app.model.schemas import IssueProcessed


class TypesenseService:
    def __init__(self) -> None:
        self.client = typesense.Client(
            {
                "nodes": [
                    {
                        "host": settings.typesense_host,
                        "port": settings.typesense_port,
                        "protocol": settings.typesense_protocol,
                    }
                ],
                "api_key": settings.typesense_api_key,
                "connection_timeout_seconds": 5,
            }
        )

        self.collection_name = settings.typesense_collection
        self.vector_dim = settings.typesense_vector_dim

        self._ensure_collection()


    def _ensure_collection(self) -> None:
        schema = {
            "name": self.collection_name,
            "fields": [
                {"name": "id", "type": "string"},
                {"name": "title", "type": "string"},
                {"name": "description", "type": "string"},
                {"name": "labels", "type": "string[]"},
                {
                    "name": "embedding",
                    "type": "float[]",
                    "num_dim": self.vector_dim,
                    "vec_dist": "cosine",
                },
            ],
        }

        try:
            self.client.collections[self.collection_name].retrieve()
        except ObjectNotFound:
            print(f"[Typesense] Creating collection '{self.collection_name}'")
            self.client.collections.create(schema)


    def upsert_issues(self, issues: List[IssueProcessed]) -> None:
        docs: List[Dict[str, Any]] = []

        for issue in issues:
            d = issue.model_dump()
            docs.append(
                {
                    "id": d["id"],
                    "title": d["title"],
                    "description": d["description"],
                    "labels": d["labels"],
                    "embedding": d["embedding"],
                }
            )

        res = self.client.collections[self.collection_name].documents.import_(
            docs, {"action": "upsert"}
        )
        print("[Typesense] IMPORT:", res)


    def get_issue(self, issue_id: str) -> Dict[str, Any]:
        return self.client.collections[self.collection_name].documents[issue_id].retrieve()


    def search_similar(
        self,
        embedding: List[float],
        limit: int = 5,
        exclude_id: Optional[str] = None,
    ) -> List[Dict[str, Any]]:

        if not embedding or len(embedding) != self.vector_dim:
            return []

        k = limit + (1 if exclude_id else 0)

        # Используем прямой HTTP запрос через httpx для векторного поиска
        base_url = f"{settings.typesense_protocol}://{settings.typesense_host}:{settings.typesense_port}"
        search_url = f"{base_url}/collections/{self.collection_name}/documents/search"
        
        headers = {
            "X-TYPESENSE-API-KEY": settings.typesense_api_key,
            "Content-Type": "application/json",
        }

        # Формат для Typesense: vector_query с именем поля как ключ
        search_body = {
            "q": "*",
            "vector_query": {
                "embedding": {
                    "vector": embedding,
                    "k": k
                }
            },
            "limit": k,
            "include_fields": "id,title,description",
        }
        
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.post(
                    search_url,
                    headers=headers,
                    json=search_body
                )
                response.raise_for_status()
                res = response.json()
                hits = res.get("hits", [])
                    
        except httpx.HTTPStatusError as e:
            print(f"[Typesense] HTTP ERROR {e.response.status_code}: {e.response.text}")
            return []
        except Exception as e:
            print(f"[Typesense] ERROR: {type(e).__name__}: {e}")
            return []

        out: List[Dict[str, Any]] = []

        for h in hits:
            if not isinstance(h, dict):
                continue
                
            doc = h.get("document", {})
            doc_id = doc.get("id")
            
            if exclude_id and doc_id == exclude_id:
                continue

            out.append(
                {
                    "id": doc_id,
                    "title": doc.get("title"),
                    "description": doc.get("description"),
                    "distance": h.get("vector_distance"),
                }
            )

            if len(out) >= limit:
                break

        return out


_service: Optional[TypesenseService] = None


def get_typesense_client() -> TypesenseService:
    global _service
    if _service is None:
        print("[Typesense] Initializing service...")
        _service = TypesenseService()
    return _service