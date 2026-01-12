from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.model.schemas import IssueIn, RecommendationResponse
from app.pipeline.pipeline import IssuePipeline
from app.services.typesense_service import get_typesense_client, TypesenseService
from app.services.recommendation_service import RecommendationService

router = APIRouter()
_pipeline = IssuePipeline()


def get_recommendation_service(
    ts: TypesenseService = Depends(get_typesense_client),
) -> RecommendationService:
    return RecommendationService(ts)


@router.post(
    "/issues",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Принимает issues, прогоняет через пайплайн и грузит в Typesense",
)
async def ingest_issues(
    issues: List[IssueIn],
    ts: TypesenseService = Depends(get_typesense_client),
):
    if not issues:
        raise HTTPException(status_code=400, detail="Empty issues list")

    processed = _pipeline.process_batch(issues)

    valid_docs = [
        p for p in processed
        if p.embedding and len(p.embedding) == ts.vector_dim
    ]
    if not valid_docs:
        raise HTTPException(status_code=400, detail="No valid embeddings to ingest")

    ts.upsert_issues(valid_docs)

    return {"status": "ok", "count": len(valid_docs)}


@router.get(
    "/recommendations",
    response_model=RecommendationResponse,
    summary="Строит рекомендации по issue и шлет дальше по API",
)
async def get_recommendations(
    issue_id: str = Query(..., description="ID базового issue"),
    limit: int = Query(5, ge=1, le=50),
    service: RecommendationService = Depends(get_recommendation_service),
):
    base_issue = service.ts.get_issue(issue_id)
    if not base_issue or "embedding" not in base_issue:
        raise HTTPException(status_code=404, detail="Issue not found or embedding missing")

    try:
        payload = service.build_recommendations(issue_id=issue_id, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    await service.forward_recommendations(payload)
    return payload


@router.get(
    "/collections",
    summary="Показывает список коллекций Typesense",
)
async def list_collections(
    ts: TypesenseService = Depends(get_typesense_client),
):
    collections = ts.client.collections.retrieve()
    return [
        {"name": c["name"], "num_documents": c.get("num_documents", 0)}
        for c in collections
    ]