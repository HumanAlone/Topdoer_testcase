FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY incident_tracker/ ./incident_tracker/

EXPOSE 8000

CMD ["uvicorn", "incident_tracker.app:app", "--host", "0.0.0.0", "--port", "8000"]