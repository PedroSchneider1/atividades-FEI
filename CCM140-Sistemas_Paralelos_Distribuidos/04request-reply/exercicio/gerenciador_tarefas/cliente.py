import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

def criar_tarefa(tarefa: dict):
    return 0

def listar_tarefas(): -> list[dict]
    return 0

def remover_tarefa(id: int):
    return 0

# adiciona tarefa 1 e 2
for i in range(1,3):
    tarefa = {
        "name": f"tarefa{i}",
        "id": (10 + i),
    }
    criar_tarefa(tarefa)

# lista tarefas [1,2]
listar_tarefas()

# remove tarefa 1
remover_tarefa(11)

# lista tarefas [1]
listar_tarefas()