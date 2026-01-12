# syntax=docker/dockerfile:1

FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app

FROM base AS deps

COPY --from=ghcr.io/astral-sh/uv:0.4.20 /uv /bin/uv

COPY pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev

FROM deps AS build

COPY app ./app

FROM base AS runtime

ENV PATH="/app/.venv/bin:$PATH" \
    EMBED_MODEL=/app/models/fine_tuned

COPY --from=deps /app/.venv /app/.venv
COPY --from=build /app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]