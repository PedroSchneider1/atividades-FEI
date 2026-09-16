import zmq
import random
from time import sleep

random.seed()

ctx = zmq.Context()

# envio de mensagens para os workers
sender = ctx.socket(zmq.PUSH)
sender.bind("tcp://*:5555")

# sincronização com o sink
sink = ctx.socket(zmq.PUSH)
sink.connect("tcp://sink:5556")

print("pronto para enviar")
sleep(2)
print("fim do sleep")
sink.send(b'0') # avisa o sink que os dados serão enviados
total = 0
tasks = 100
for task in range(tasks):
    workload = random.randint(1, 100) # a tarefa é esperar o tempo de workload
    total += workload
    sender.send_string(f"{workload}")
print(f"Custo total: {total}ms")
sleep(1)
