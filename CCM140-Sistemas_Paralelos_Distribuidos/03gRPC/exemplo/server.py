from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def HelloWorld(self, request, context):
        print(f"Mensagem do cliente: {request.mensagem}")
        return helloworld_pb2.MsgServidor(mensagem="World")

endereco = "[::]:50051"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), servidor)
servidor.add_insecure_port(endereco)
servidor.start()

print(f"Servidor escutando em {endereco}")
servidor.wait_for_termination()