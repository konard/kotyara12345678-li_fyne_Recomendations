from typing import List, Dict, Any
import math

from app.model.schemas import RecommendationItem, RecommendationResponse, ForwardPayload
from app.services.typesense_service import TypesenseService
from app.core.config import settings
import httpx


class RecommendationService:
    def __init__(self, ts: TypesenseService):
        self.ts = ts

    @staticmethod
    def _normalize_embedding(embedding: List[float]) -> List[float]:
        """Нормализует эмбеддинг (делает длину вектора = 1)"""
        if not embedding:
            return embedding
        
        # Вычисляем длину вектора
        magnitude = math.sqrt(sum(x * x for x in embedding))
        
        if magnitude == 0:
            raise ValueError("Cannot normalize zero vector")
        
        # Нормализуем
        normalized = [x / magnitude for x in embedding]
        return normalized

    def build_recommendations(self, issue_id: str, limit: int) -> RecommendationResponse:
        base_issue = self.ts.get_issue(issue_id)
        if not base_issue:
            raise ValueError("Base issue not found")

        embedding = base_issue.get("embedding")
        if not embedding:
            raise ValueError("Embedding not found in base issue")
        
        # Нормализуем эмбеддинг, если не нормализован
        if isinstance(embedding, list) and len(embedding) > 0:
            magnitude = math.sqrt(sum(x * x for x in embedding))
            if abs(magnitude - 1.0) > 0.01:
                embedding = self._normalize_embedding(embedding)

        similar_docs = self.ts.search_similar(
            embedding=embedding,
            limit=limit,
            exclude_id=issue_id,
        )

        recommendations = [
            RecommendationItem(
                id=doc["id"],
                score=doc["distance"],
                title=doc.get("title"),
                description=doc.get("description"),
            )
            for doc in similar_docs
        ]

        return RecommendationResponse(
            base_issue_id=issue_id,
            recommendations=recommendations,
        )

    async def forward_recommendations(self, payload: RecommendationResponse):
        if not settings.forward_url:
            return

        data = ForwardPayload(
            issue_id=payload.base_issue_id,
            recommendations=payload.recommendations,
        )

        async with httpx.AsyncClient() as client:
            try:
                await client.post(settings.forward_url, json=data.model_dump())
            except Exception as e:
                print("Forwarding failed:", e)