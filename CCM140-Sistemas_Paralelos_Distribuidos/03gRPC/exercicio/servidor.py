import grpc
import taskmanager_pb2
import taskmanager_pb2_grpc
from concurrent import futures

class TaskManagerService(taskmanager_pb2_grpc.TaskManagerServicer):
    def __init__(self):
        self.tasks = {}
        self.counter = 0

    def ConnectionTest(self, request, context):
        print(f"Mensagem do cliente: {request.message}",flush=True)
        return taskmanager_pb2.ConnReply(message="ACK")

    def Create(self, request, context):
        self.counter += 1
        id = str(self.counter)
        task = taskmanager_pb2.Task(id=id, title=request.title, description=request.description, status="não completo")
        self.tasks[id] = task
        return task

    def Get(self, request, context):
        id = request.id
        if id in self.tasks:
            return self.tasks[id]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "ERRO: tarefa não encontrada")

    def List(self, request, context):
        return taskmanager_pb2.ListResponse(tasks=self.tasks.values())

    def Update(self, request, context):
        id = request.id
        if id in self.tasks:
            task = self.tasks[id]
            task.title = request.title
            task.description = request.description
            task.status = request.status
            return task
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "ERRO: tarefa não encontrada")

    def Delete(self, request, context):
        id = request.id
        if id in self.tasks:
            del self.tasks[id]
            return taskmanager_pb2.Empty()
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "ERRO: tarefa não encontrada")

endereco = "[::]:50051"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
taskmanager_pb2_grpc.add_TaskManagerServicer_to_server(TaskManagerService(), servidor)

servidor.add_insecure_port(endereco)
servidor.start()
print(f"Servidor escutando em {endereco}", flush=True)
servidor.wait_for_termination()