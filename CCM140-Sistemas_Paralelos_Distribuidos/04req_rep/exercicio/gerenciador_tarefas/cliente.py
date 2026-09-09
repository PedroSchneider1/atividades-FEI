import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

CRIAR_TAREFA = b"criar_"
REMOVER_TAREFA = b"remover_"
LISTAR_TAREFAS = b"listar_"

def criar_tarefa(tarefa: dict) -> bytes:
    socket.send(bytearray(CRIAR_TAREFA + str(tarefa).encode()))
    response = socket.recv()
    return response

def remover_tarefa(id: int) -> bytes:
    socket.send(bytearray(REMOVER_TAREFA + str(id).encode()))
    response = socket.recv()
    return response

def listar_tarefas() -> list[dict]:
    socket.send(LISTAR_TAREFAS)
    response = socket.recv()
    return eval(response.decode())


# adiciona tarefa 1 e 2
for i in range(1,3):
    print(f"Enviando tarefa {i} para o servidor...")
    tarefa = {
        "name": f"tarefa{i}",
        "id": i,
    }
    print(criar_tarefa(tarefa).decode())

# teste erro
print("Enviando comando inválido para o servidor...")
socket.send(b"comando_invalido")
response = socket.recv()
print(f"Resposta do servidor: {response.decode()}")

# lista tarefas [1,2]
print(listar_tarefas())

# remove tarefa 1
print(remover_tarefa(id=1).decode())

# lista tarefas [1]
print(listar_tarefas())

socket.close()
context.close()