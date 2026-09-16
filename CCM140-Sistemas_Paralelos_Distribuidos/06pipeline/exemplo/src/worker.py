import time
import zmq

ctx = zmq.Context()

# recebe mensagem do ventilator
receiver = ctx.socket(zmq.PULL)
receiver.connect("tcp://ventilator:5555")

# envia mensagem para o sink
sender = ctx.socket(zmq.PUSH)
sender.connect("tcp://sink:5556")

while True:
    workload = receiver.recv_string()
    #print(f"Tempo: {workload}ms")
    time.sleep(int(workload)*0.001) # simula a execução da tarefa
    sender.send_string(f"{workload}") # envia resultado para o sink
