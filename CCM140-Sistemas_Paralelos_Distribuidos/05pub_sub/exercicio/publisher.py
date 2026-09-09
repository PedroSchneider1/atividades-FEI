import zmq
import os
import time
import random

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

tipo = os.getenv("TYPE")

while True:
    hora = f"hora {time.strftime('%H:%M:%S')}"
    numero = f"numero {random.randint(1, 6)}"

    if tipo == "hora":
        print(f"Enviando: {hora}")
        pub.send_string(f"hora {hora}")
    elif tipo == "numero":
        print(f"Enviando: {numero}")
        pub.send_string(f"numero {numero}")
    elif tipo == "geral":
        mensagem = f"GERAL:\t{hora}\n\t{numero}"
        print(f"Enviando: {mensagem}")
        pub.send_string(f"geral {mensagem}")
    else:
        raise ValueError("TYPE deve ser 'hora' ou 'numero' ou 'geral")

    time.sleep(1)

pub.close()
context.close()
