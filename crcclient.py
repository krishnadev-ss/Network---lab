import socket


IP = "127.0.0.1"
PORT = 8085
KEY = "1001"


def xor(a,b):
    result = []
    for i in range(1,len(a)):
        if a[i]==b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)

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

def encrypt(data):
    klen = len(KEY)
    appended_data= data + "0"*(klen - 1)
    remainder = mod2div(appended_data)
    codeword = data + remainder
    return codeword


def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((IP,PORT))
    message = input("enter message:")
    message = encrypt(message)
    print("encrypted message: ",message)
    client.send(message.encode("utf-8"))
    client.close()

main()

