import zmq
import os
import time
import random

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy_lab:5555")

while True:
    hora = f"{time.strftime('%H:%M:%S')}"
    numero = f"{random.randint(1, 6)}"

    print(f"Enviando: {hora}")
    pub.send_string(f"hora {hora}")
    print(f"Enviando: {numero}")
    pub.send_string(f"numero {numero}")

    time.sleep(1)

pub.close()
context.close()
