import socket
import threading
host = '127.0.0.1'
port = 8087

alias = input("enter a username:")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))


def client_recieve():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "alias?":
                client.send(alias.encode("utf-8"))
            else:
                print(message)
        except:
            print("error")
            client.close()
            break

def client_send():
    while True:
        message = input("")
        if message.startswith("@"):
            recipient_alias, message_content = message.split(" ",1)
            private_message = f'{recipient_alias} {message_content}'
            client.send(private_message.encode("utf-8"))
        else:
            client.send(message.encode('utf-8'))


recieve_thread = threading.Thread(target= client_recieve)
recieve_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()