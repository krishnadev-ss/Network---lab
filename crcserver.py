import socket

IP = "127.0.0.1"
PORT = 8085
KEY = "1001"

def decrypt(data):
    klen = len(KEY)
    appended_data = data + "0" *(klen-1)
    remainder = mod2div(appended_data)
    return remainder
def mod2div(data):
    klen = len(KEY)
    cipher = data[0:klen]
    while klen < len(data):
        if cipher[0] == "1":
            cipher = xor(cipher,KEY) + data[klen]
        else:
            cipher = xor(cipher,"0"*klen)+data[klen]
        klen+=1
    
    if cipher[0] == "1":
        cipher = xor(cipher,KEY)
    else:
        cipher = xor(cipher,"0"*klen)
    return cipher

def xor(a,b):
    result = []
    for i in range(1,len(a)):
        if a[i]==b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)


def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    client,addr = server.accept()
    data = client.recv(1024).decode("utf-8")
    if data:
        print("Receieved: ",data)
        data = decrypt(data)
        print("remainder:",data)
        check = "0"*(len(KEY)-1)
        if data == check:
            print("no error found")
        else:
            print("error")
    server.close()

main()
        