# ---------- Stage 1: Build dependencies ----------
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build deps only in this stage — they never reach the final image
COPY app/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim AS runtime

# Non-root user — never run the app as root in the container
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Bring in only the installed packages, not build tools/caches
COPY --from=builder /root/.local /home/appuser/.local
COPY app/src ./src

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Container-level health check, separate from the pipeline's post-deploy check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
