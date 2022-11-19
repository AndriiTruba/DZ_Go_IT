import socket

TCP_IP = 'localhost'
TCP_PORT = 8080


def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        server = ip, port
        client_socket.connect(server)
        print(f"Client socket run ({ip} : {port})")
        message = input('>> ').lower().strip()
        if len(message) > 0:
            while message != 'exit':
                client_socket.send(message.encode())
                message_from_server = client_socket.recv(256).decode()
                print(f"Received notification: {message_from_server}")
                print(f"To exit enter: 'exit'")
                message = input('>> ').lower().strip()
                if len(message) == 0:
                    break
    print(f'Data transfer completed')


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)
