import socket

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET  ,socket.SO_REUSEADDR,1)
server_socket.bind((IP,PORT))

server_socket.listen()

socket_list = [server_socket]

client_socket , address = server_socket.accept()

username = client_socket.recv(1024).decode('utf-8')

print(f"{username} has connected")

while True:
    message = client_socket.recv(1024).decode('utf-8')

    if not message:
        print(f"{username} has disconncted")
        break
    print(f'{username}:{message}')
    server_message = input('server: ')
    client_socket.send(server_message.encode('utf-8'))



