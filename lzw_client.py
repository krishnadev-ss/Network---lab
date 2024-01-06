import socket
import pickle

def lzw_decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    result = [chr(compressed_data[0])]
    current_code= 256
    current_sequence = chr(compressed_data[0])

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == current_code:
            entry = current_sequence +current_sequence[0]
        else:
            raise ValueError("invalid compressed data")

        result.append(entry)
        dictionary[current_code]= current_sequence+entry[0]
        current_code += 1
        current_sequence = entry
    return ''.join(result)




def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',12346))

    input_data = input("enter the data tp send:")
    client.send(input_data.encode())
    print("data sent to server:",input_data)


    compressed_data_pickle = client.recv(1024)
    compressed_data = pickle.loads(compressed_data_pickle)
    print("compressed data recieved from server:",compressed_data)


    decompressed_data = lzw_decompress(compressed_data)
    print("decompresses data:",decompressed_data)

    if input_data == decompressed_data:
        print("no errors")
    else:
        print("data recieved has errors")
    client.close()

main()