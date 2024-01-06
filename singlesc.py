import socket

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((IP,PORT))

username = input("enter a message:")
client_socket.send(username.encode('utf-8'))

while True:
    message = input(f'{username}:')
    client_socket.send(message.encode('utf-8'))
    message = client_socket.recv(1024).decode('utf-8')
    print(f'server : {message}')