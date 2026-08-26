import grpc
import helloworld_pb2
import helloworld_pb2_grpc

print("Cliente conectando com servidor")
porta = "50051"
endereco = "localhost"

with grpc.insecure_channel(f"{endereco}:{porta}") as channel:
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    resposta = stub.HelloWorld(helloworld_pb2.MsgCliente(mensagem="hello"))
    print(f"Resposta do servidor: {resposta.mensagem}")