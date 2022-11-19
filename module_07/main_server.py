import socket

TCP_IP = 'localhost'
TCP_PORT = 8080


def run_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(2)
    print(f'Start echo server {server_socket.getsockname()}')
    new_sock, address = server_socket.accept()
    try:
        while True:
            message_from_client = new_sock.recv(256).decode()
            if not message_from_client:
                print(message_from_client, 'Data transfer completed')
                break
            print(f"Received notification: {message_from_client}")
            message = "Oк!"
            new_sock.send(message.encode())
    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        server_socket.close()


if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)
