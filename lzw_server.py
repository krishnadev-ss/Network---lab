import socket
import pickle

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    print("recieved data:",data)

    compressed_data = lzw_compress(data)
    compressed_data_pickle = pickle.dumps(compressed_data)
    client_socket.send(compressed_data_pickle)
    print("compressed data sent to client")
    client_socket.close()

def lzw_compress(data):
    dictionary = {chr(i):i for i in range(256)}
    result = []
    current_code = 256
    current_sequence = ""

    for char in data:
        current_sequence+=char
        if current_sequence not in dictionary:
            result.append(dictionary[current_sequence[:-1]])
            dictionary[current_sequence] = current_code
            current_code+=1
            current_sequence = char
    if current_sequence in dictionary:
    
       result.append(dictionary[current_sequence])
    return result
'''
    print("dictionary:")
    for key, value in dictionary.items():  # Corrected loop syntax
        if dictionary:  # Separate if statement
            print(f"{key}: {value}")
    
'''
def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',12346))
    server.listen(1)
    print("server is listening")

    while True:
        client_socket , address = server.accept()
        print("accepted connection from ",address)
        handle_client(client_socket)


main()