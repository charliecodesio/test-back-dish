FROM python:3.11-slim-bookworm

# Evita prompts interactivos al instalar
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza paquetes del sistema y limpia caché
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends gcc build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
