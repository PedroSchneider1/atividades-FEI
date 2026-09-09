import zmq
import os
from time import sleep

context = zmq.Context()
sub = context.socket(zmq.SUB)

topic = os.getenv("TOPIC")

sub.connect(f"tcp://proxy:5556")
sub.setsockopt_string(zmq.SUBSCRIBE, topic)

while True:
    mensagem = sub.recv_string()
    print(f"Recebido: {mensagem}")

sub.close()
context.close()
