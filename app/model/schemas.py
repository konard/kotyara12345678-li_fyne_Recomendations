from typing import List, Optional
from pydantic import BaseModel, Field


class IssueIn(BaseModel):
    id: str
    title: str
    body: Optional[str] = None
    labels: Optional[List[str]] = None


class IssueProcessed(BaseModel):
    id: str
    title: str
    description: str
    labels: List[str] = Field(default_factory=list)
    embedding: List[float]  


class RecommendationItem(BaseModel):
    id: str
    score: float
    title: Optional[str] = None
    description: Optional[str] = None


class RecommendationResponse(BaseModel):
    base_issue_id: Optional[str] = None
    recommendations: List[RecommendationItem]


class ForwardPayload(BaseModel):
    issue_id: str
    recommendations: List[RecommendationItem]