FROM python:3.9-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

COPY requirements.txt .
RUN pip install --no-cache-dir 'setuptools<81' && \
    pip install --no-cache-dir -r requirements.txt && \
    useradd --uid 1001 --create-home appuser

COPY service ./service
USER appuser
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--access-logfile", "-", "service:app"]
