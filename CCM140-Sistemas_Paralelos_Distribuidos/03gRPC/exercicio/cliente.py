import json

import grpc
import taskmanager_pb2
import taskmanager_pb2_grpc
from google.protobuf.json_format import MessageToJson

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

print("Cliente conectando com o servidor",flush=True)
porta = "50051"
endereco = "servidor"
channel = grpc.insecure_channel(f"{endereco}:{porta}")
stub = taskmanager_pb2_grpc.TaskManagerStub(channel)

print("Inicializando FastAPI", flush=True)
app = FastAPI()

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    status: str

@app.get("/")
def list_tasks():
    request = taskmanager_pb2.ListRequest()
    response = MessageToJson(stub.List(request))
    return JSONResponse(content=json.loads(response))

@app.get("/test")
def connection_test():
    print("Testando conexão com servidor")
    request = taskmanager_pb2.ConnRequest(message="SYN")
    response = stub.ConnectionTest(request)
    return response.message

@app.put("/adicionar/")
def create_task(tarefa: Tarefa):
    request = taskmanager_pb2.CreateRequest(
        title=tarefa.titulo,
        description=tarefa.descricao,
    )
    response = stub.Create(request)
    return response.id

@app.get("/tarefa/{pos}")
def get_task(id: int):
    request = taskmanager_pb2.GetRequest(id=str(id))
    try:
        response = MessageToJson(stub.Get(request))
        return JSONResponse(content=json.loads(response))
    except grpc.RpcError as e:
        print(e.details(), flush=True)


@app.put("/atualizar/")
def update_task(tarefa: Tarefa, id: int):
    request = taskmanager_pb2.UpdateRequest(
        id=str(id),
        title=tarefa.titulo,
        description=tarefa.descricao,
        status=tarefa.status
    )
    try:
        response = stub.Update(request)
        print(f"Tarefa atualizada: {response}", flush=True)
    except grpc.RpcError as e:
        print(e.details(), flush=True)

@app.delete("/deletar/{pos}")
def delete_task(id: int):
    request = taskmanager_pb2.DeleteRequest(id=str(id))
    try:
        stub.Delete(request)
        return "Tarefa apagada"
    except grpc.RpcError as e:
        print(e.details(), flush=True)