import socket

SERVER = "*.*.*"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("listener", 'UTF-8'))
in_data = client.recv(1024)
print("From Server :", in_data.decode())
while True:
    out_data = input("Enter something:")
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        break
    #in_data=str(in_data.decode())
    #print("From Server :",in_data)
client.close()
