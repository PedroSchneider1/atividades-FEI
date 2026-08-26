FROM python:3.13.7-alpine3.21

WORKDIR /app

RUN pip install grpcio grpcio-tools

COPY ./helloworld.proto .

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto

CMD ["python", "main.py"]
