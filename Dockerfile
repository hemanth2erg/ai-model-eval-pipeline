FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pydantic
CMD ["python", "main.py"]
