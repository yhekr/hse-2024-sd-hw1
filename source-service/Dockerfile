FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ /app/

ENV PYTHONPATH=/app

EXPOSE 50051

CMD ["python", "services/grpc_server_runner.py"]