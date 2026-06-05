# ── base ──────────────────────────────────────────────────────
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

COPY pyproject.toml .
COPY . .

# ── api ───────────────────────────────────────────────────────
FROM base AS api

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ── crawler ───────────────────────────────────────────────────
FROM base AS crawler

RUN uv sync --no-dev

CMD ["uv", "run", "python", "-m", "crawler.flows.entrypoint"]
