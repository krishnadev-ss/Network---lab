import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),1235))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)

while True:
    clientsocket , address = s.accept()
    print(f"connection from {address} has been established ")

    clientsocket.send(f"welcome to the server".encode("utf-8"))
    clientsocket.close()