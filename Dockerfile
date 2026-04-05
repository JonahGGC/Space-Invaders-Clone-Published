# ── Stage 1: builder ──────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder
 
WORKDIR /app
 
# Install dependencies into a separate prefix so we can copy them cleanly
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt
 
 
# ── Stage 2: runtime ──────────────────────────────────────────────────────────
FROM python:3.11-slim AS runtime
 
WORKDIR /app
 
# Copy installed packages from builder
COPY --from=builder /install /usr/local
 
# Copy application source
COPY main.py .
 
# Copy the Unity WebGL build (static files served by FastAPI)
COPY WebGame/ ./WebGame/
 
# Non-root user for safety
RUN adduser --disabled-password --gecos "" appuser
USER appuser
 
EXPOSE 8000
 
# Uvicorn with 1 worker is fine for a game server;
# scale up with --workers N if needed
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]