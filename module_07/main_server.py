import socket
from time import sleep

TCP_IP = 'localhost'
TCP_PORT = 8080


def main(host, port):
    while True:
        message_from_client = run_server(host, port)
        if message_from_client == 'exit':
            print(f'Data transfer completed')
            break
        message_from_server = run_client(host, port)
        if message_from_server:
            print(f'Data transfer completed')
            break


def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    new_sock, address = server_socket.accept()
    print(f"Server socket run ({host} : {port})")
    try:
        message_from_client = new_sock.recv(256).decode()
        if message_from_client == 'exit':
            return message_from_client
        print(f"From client: {message_from_client}")
        print(f"To exit enter: 'exit'")
        message = "Oк!"
        new_sock.send(message.encode())

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        server_socket.close()


def run_client(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            server = host, port
            client_socket.connect(server)
            print(f"Client socket run ({host} : {port})")
            while True:
                message = input('>> ').lower().strip()
                client_socket.send(message.encode())
                message_from_server = client_socket.recv(256).decode()
                print(f"From server: {message_from_server}")
                if message_from_server == "Oк!":
                    return message_from_server
        except ConnectionRefusedError:
            sleep(0.5)


if __name__ == '__main__':
    main(TCP_IP, TCP_PORT)
