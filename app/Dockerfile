# ---- Build stage ----
FROM python:3.14.6-alpine3.24 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---- Final stage ----
FROM python:3.14.6-alpine3.24

# Update affected runtime libraries from the configured Alpine repositories
RUN apk upgrade --no-cache libcrypto3 libssl3 libuuid

# Alpine uses busybox — no groupadd/useradd; use addgroup/adduser instead
RUN addgroup -g 1000 appuser && \
    adduser -D -H -u 1000 -G appuser -s /sbin/nologin appuser

WORKDIR /app

COPY --from=builder /root/.local /home/appuser/.local
COPY app.py .

ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER 1000:1000

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "30", "--worker-tmp-dir", "/tmp", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
