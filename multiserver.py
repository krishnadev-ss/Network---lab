import socket
import threading


host = '127.0.0.1'
port = 8087


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)

clients = {}
alaises = {}

def broadcast(message):
    for client_socket in clients:
        client_socket.send(message)

def handle_client(client_socket):
    alias = alaises[client_socket]
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                if message.startswith('@'):
                    recipient_alias,message_content = message.split(' ',1)
                    recipient_socket = None
                    recipient_alias = recipient_alias[1:].lower()
                    for socket,username in alaises.items():
                        if username.lower() == recipient_alias:
                            recipient_socket = socket
                            break

                    if recipient_socket:
                        recipient_socket.send(f"{alias} (private): {message_content}".encode("utf-8"))
                    else:
                        client_socket.send(f"user '@{recipient_alias}' not found or offline ".encode('utf-8'))
                else:
                    broadcast(f'{alias}:{message}'.encode("utf-8"))
        except:
            alias = alaises[client_socket]
            del alaises[client_socket]
            clients.pop(client_socket)
            broadcast(f'{alias} has left the chat room'.encode('utf-8'))
            break






def recieve():
    while True:
        print("seerver is listening...")
        client_socket,address = server.accept()
        print(f"connection is established with {address}")
        client_socket.send('alias?'.encode('utf-8'))
        alias = client_socket.recv(1024).decode('utf-8')
        alaises[client_socket] = alias
        clients[client_socket] = True
        print(f"the alias of the client is {alias}")
        broadcast(f"{alias} is connected to the chat room".encode("utf-8"))
        client_socket.send("you are now connected ".encode("utf-8"))
        thread = threading.Thread(target = handle_client,args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    recieve()
