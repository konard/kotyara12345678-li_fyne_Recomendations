from typing import List

import math

from app.model.schemas import IssueIn, IssueProcessed
from app.pipeline.steps import normalize_text, build_embedding


class IssuePipeline:

    def process_one(self, issue: IssueIn) -> IssueProcessed:
        title = normalize_text(issue.title)
        description = normalize_text(issue.body or "")
        labels = issue.labels or []

        raw_embedding = build_embedding(title, description)

        embedding = self._sanitize_embedding(raw_embedding)

        return IssueProcessed(
            id=issue.id,
            title=title,
            description=description,
            labels=labels,
            embedding=embedding,
        )

    def process_batch(self, issues: List[IssueIn]) -> List[IssueProcessed]:
        return [self.process_one(issue) for issue in issues]

    @staticmethod
    def _sanitize_embedding(raw_embedding) -> List[float]:
        if raw_embedding is None:
            raise ValueError("Embedding is None")

        if hasattr(raw_embedding, "tolist"):
            raw_embedding = raw_embedding.tolist()

        embedding = [float(x) for x in raw_embedding]

        from app.core.config import settings
        if len(embedding) != settings.typesense_vector_dim:
            raise ValueError(f"Invalid embedding size: {len(embedding)}")

        if any(
            math.isnan(x) or math.isinf(x)
            for x in embedding
        ):
            raise ValueError("Embedding contains NaN or Inf")

        if all(x == 0.0 for x in embedding):
            raise ValueError("Zero embedding detected")

        return embedding