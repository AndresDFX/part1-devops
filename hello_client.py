import grpc
import hello_pb2
import hello_pb2_grpc


def run():
    with grpc.insecure_channel('grpc-server:50051') as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)

        # Método unario
        response = stub.SayHelloSimple(hello_pb2.HelloRequest(name='world'))
        print("gRPC client received:", response.message)

        # Streaming del servidor
        responses = stub.SayHelloServerStream(hello_pb2.HelloRequest(name='world'))
        for response in responses:
            print("gRPC client received:", response.message)

        # Streaming del cliente
        response = stub.SayHelloClientStream(
            iter([hello_pb2.HelloRequest(name=name) for name in ["Alice", "Bob", "Charlie"]]))
        print("gRPC client received:", response.message)

        # Streaming bidireccional
        responses = stub.SayHelloBidirectional(
            iter([hello_pb2.HelloRequest(name=name) for name in ["Alice", "Bob", "Charlie"]]))
        for response in responses:
            print("gRPC client received:", response.message)


if __name__ == "__main__":
    run()
