# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set default entrypoint for containers that don't override it
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
