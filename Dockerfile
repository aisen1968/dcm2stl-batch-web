FROM python:3.11-slim

WORKDIR /app

COPY backend/ backend/
COPY frontend/ frontend/

RUN pip install --no-cache-dir -r backend/requirements.txt

# Aquí se copiaría o instalaría Open3SDCM
# RUN apt-get install -y open3sdcm

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "80"]
