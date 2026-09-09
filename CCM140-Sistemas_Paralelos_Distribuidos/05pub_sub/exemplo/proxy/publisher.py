import zmq
from time import time, sleep

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    message = str(time())
    print(f"message: {message}", flush=True)
    pub.send_string(message)
    sleep(1)

pub.close()
context.close()
