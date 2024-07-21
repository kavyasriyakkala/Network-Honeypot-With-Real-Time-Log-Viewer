import socket
from datetime import datetime

def start_honeypot():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 8080)
    print(f'Starting honeypot on {server_address[0]} port {server_address[1]}')
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print('Waiting for a connection...')
        connection, client_address = sock.accept()
        try:
            print(f'Connection from {client_address}')
            while True:
                data = connection.recv(16)
                if data:
                    print(f'Received "{data}" from {client_address}')
                    log_attack(client_address, data)
                else:
                    break
        finally:
            connection.close()

def log_attack(client_address, data):
    with open('honeypot.log', 'a') as log_file:
        log_file.write(f'{datetime.now()} - {client_address[0]}:{client_address[1]} - {data}\n')
        print(f'Logged attack from {client_address}')

if __name__ == '__main__':
    start_honeypot()
