from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tarefas = list()

class Tarefa(BaseModel):
    tarefa: str
    prioridade: int
    feito: bool

@app.get("/")
def root():
    return tarefas

@app.get("/tarefa/{pos}")
def get_tarefa(pos: int):
    return tarefas[pos]

@app.post("/adicionar/")
def criar_tarefa(tarefa: Tarefa):
    tarefa.feito = False
    tarefas.append(tarefa)
    return len(tarefas)

@app.put("/feito/{pos}")
def marcar_feito(pos: int):
    tarefas[pos].feito = True
    return tarefas[pos]

@app.delete("/deletar/{pos}")
def deletar_tarefa(pos: int):
    tarefa = tarefas.pop(pos)
    return tarefa