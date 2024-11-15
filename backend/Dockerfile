FROM python:3.9-slim

WORKDIR /app
COPY backend.py requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "backend.py"]
