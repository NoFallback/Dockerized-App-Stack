FROM python:3.12-slim
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY app.py .
ENV HOST=0.0.0.0
ENV PORT=8000
EXPOSE 8000
CMD ["python", "app.py"]
