import zmq
import os

context = zmq.Context()
sub = context.socket(zmq.SUB)

topic = os.getenv("TOPIC")

sub.connect("tcp://proxy_lab:5556")

if topic == "geral":
    sub.setsockopt_string(zmq.SUBSCRIBE, "hora")
    sub.setsockopt_string(zmq.SUBSCRIBE, "numero")
else:
    sub.setsockopt_string(zmq.SUBSCRIBE, topic)

while True:
    mensagem = sub.recv_string()
    print(f"Recebido: {mensagem}")

sub.close()
context.close()
