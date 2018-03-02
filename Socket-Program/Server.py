import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def ClientListener(self):
        print("Connect to a client")
        res = 'Got connected'
        while True:
            self.csocket.send(bytes(res, 'UTF-8'))
            # data = self.csocket.recv(2048)
            # msg = data.decode()
            res = input("Enter the msg:")
            # print("from client", res)
            self.csocket.send(bytes(res, 'UTF-8'))
            if res == 'bye':
                break
        print("Client at ", clientAddress, " disconnected...")

    def DataListener(self):
        print("Connect to a listner")
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        res = 'Got connected'
        self.csocket.send(bytes(res, 'UTF-8'))
        while True:
            #self.csocket.send(bytes(res, 'UTF-8'))
            data = self.csocket.recv(2048)
            msg = data.decode()
            #res = input("Enter the msg:")
            print("from client", msg)
            self.csocket.send(bytes(res, 'UTF-8'))
            if msg == 'bye':
                break
        print("Listener at ", clientAddress, " disconnected...")


    def FileTransfer(self,filename):
        print('Server listening....')

        while True:
            f = open(filename, 'rb')
            l = f.read(1024)
            while (l):
                self.csocket.send(l)
                print('Sent ', repr(l))
                l = f.read(1024)
            f.close()
            print('Done sending')



    def run(self):
        print("Connection from : ", clientAddress)
        data = self.csocket.recv(2048)
        info = str(data.decode())
        if info == "client":
            self.ClientListener()

        if info == "listener":
            self.DataListener()

        if info == "file-transfer":
            self.FileTransfer()



LOCALHOST = "192.168.0.8"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()


