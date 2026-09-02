import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

while True:
    message = socket.recv()
    print(f"Mensagem recebida: {message}", flush=True)
    socket.send_string("World")

