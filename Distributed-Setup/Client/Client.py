import socket
import subprocess
import fileinput
import sys
import argparse


global jmeterPath
global filePath
import os
dir_name = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser()
parser.add_argument("--jmeterPath", help="Execute JMeter")
parser.add_argument("--host", help="Start Server At")

args = parser.parse_args()

if (args.jmeterPath):
    jmeterPath = args.jmeterPath

else:
    jmeterPath = "C:\\Users\\Yajana\\apache-jmeter\\jmeter-setup\\apache-jmeter-3.3\\bin"

if args.host:
    ip = args.host

else:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

filePath = dir_name+"\\file_received.jmx"
print(filePath)
# if not sys.argv:
#     jmeterPath = "C:\\Users\\Yajana\\apache-jmeter\\apache-jmeter-3.3\\bin"
#
# if  len(sys.argv) > 1:
#     jmeterPath = sys.argv[1]


if os.path.exists(filePath):
    f = open(filePath, 'r+')
    f.truncate()

def read_n_write_ip(content):
    global jmeterPath
    #content = ", ".join(ips)
    #print(content)
    text = "remote_hosts="
    x = fileinput.input(files=jmeterPath + "\jmeter.properties", inplace=1)
    for line in x:
        if text in line:
            line = "remote_hosts=" + content + "\n"
        sys.stdout.write(line)
        #print(line)
    x.close()

def ClientListener(self):
    while True:
        # self.csocket.send(bytes(res, 'UTF-8'))
        data = self.csocket.recv(4092)
        msg = data.decode()
        #print("msg from client:", msg)
        if "EDIT" in msg:
            var = msg.split("::")
            ip = var[1]
            #print(ip)
            read_n_write_ip(ip)
            output = "Done"
            self.csocket.send(bytes(str(output), 'UTF-8'))

        elif "COMMAND::" in msg:
            var = msg.split("::")
            commmad = var[1]
            commmad = "\jmeter.bat -n -t " + filePath + commmad
            try:
                proc = subprocess.Popen(jmeterPath+commmad, shell=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = proc.communicate()
                if err:
                    output = err
                    print(err)

                else:
                    output = out
                    print(output)
            except:
                output = "Failed"

            self.csocket.send(bytes(str(output), 'UTF-8'))
            break

        else:
            f = open(filePath, "a")
            f.write(msg)
            f.close()


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
            #print("Done")

        except:
            print("Connection closed")


PORT = 8070
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', PORT))
print("Server started at "+str(ip)+":"+str(PORT))
print("Waiting for  request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    ClientThread(clientAddress, clientsock)