FROM python:3.12-slim
ENV PYTHONIOENCODING=utf-8
WORKDIR /app
COPY generator.py README.md ./
ENTRYPOINT ["python", "generator.py"]