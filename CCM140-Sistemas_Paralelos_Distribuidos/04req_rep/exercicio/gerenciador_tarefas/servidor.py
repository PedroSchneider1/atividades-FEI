import zmq
import ast

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

tarefas = []

CRIAR_TAREFA = b"criar_"
REMOVER_TAREFA = b"remover_"
LISTAR_TAREFAS = b"listar_"

while True:
    message = socket.recv()
    if message.startswith(CRIAR_TAREFA):
        print(f"Tarefa recebida: {message}", flush=True)
        tarefas.append(ast.literal_eval(message.split(b"_")[1].decode())) # ast literal_eval para converter a string de volta para um dicionário (built-in lib)
        socket.send_string("OK")
    elif message.startswith(REMOVER_TAREFA):
        print(f"Remover tarefa: {message}", flush=True)
        tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != int(message.split(b"_")[1].decode())]
        socket.send_string("OK")
    elif message.startswith(LISTAR_TAREFAS):
        print(f"Listar tarefas: {message}", flush=True)
        socket.send_string(str(tarefas))
    else:
        print(f"Mensagem desconhecida: {message}", flush=True)
        socket.send_string("ERRO: Comando desconhecido")

socket.close()
context.close()

