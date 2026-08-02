# ---- Build stage ----
FROM python:3.14.6-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---- Final stage ----
FROM python:3.14.6-slim-bookworm

# Create a non-root user and group
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/false --no-create-home appuser

WORKDIR /app

# Copy only the installed packages from the builder stage, not build tools
COPY --from=builder /root/.local /home/appuser/.local
COPY app.py .

# Make sure the non-root user's installed packages are on PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Drop root privileges
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["python", "app.py"]