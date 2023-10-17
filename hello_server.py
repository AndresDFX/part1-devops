import grpc
import hello_pb2
import hello_pb2_grpc
import time
import concurrent.futures as futures



class HelloServiceServicer(hello_pb2_grpc.HelloServiceServicer):

    def SayHelloSimple(self, request, context):
        return hello_pb2.HelloResponse(message="Hello, " + request.name)

    def SayHelloServerStream(self, request, context):
        for _ in range(5):
            yield hello_pb2.HelloResponse(message="Hello, " + request.name)
            time.sleep(1)

    def SayHelloClientStream(self, request_iterator, context):
        names = [request.name for request in request_iterator]
        return hello_pb2.HelloResponse(message="Hello, " + ", ".join(names))

    def SayHelloBidirectional(self, request_iterator, context):
        for request in request_iterator:
            yield hello_pb2.HelloResponse(message="Hello, " + request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
