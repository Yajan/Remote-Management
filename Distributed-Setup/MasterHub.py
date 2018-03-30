import socket
import threading
import time
ips = []
ips.append("")

clientInfo = {}

def ConnectSlaves(ip):
   PORT = 8070
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect((ip, PORT))
   return client

def executeCommand(ip,command):
    if ip in clientInfo:
       client = clientInfo[ip]
       client.sendall(bytes(command, 'UTF-8'))
       in_data = client.recv(4096)
       print("Replay :", in_data.decode())

def Messanger(ip,command):
    executeCommand(ip,command)

def Listner(ip,duration):
    time.sleep(duration)
    try:
        client = clientInfo[ip]
        client.close()
    except:
        print("Connection Closed")

class MasterHub():
    def __init__(self,ips,commands):
        for ip in ips:
           try:
              client = ConnectSlaves(ip)
              clientInfo[ip] = client
           except:
              print("Failed")
        print(commands)
        if clientInfo:
            print("Connected to: ")
            for keys in clientInfo.keys():
                print(keys)
                t1 = threading.Thread(target=Messanger, args=(keys,commands,))
                #t2 = threading.Thread(target=Listner,args=(keys,duration,))
                t1.start()
                #t2.start()




MasterHub(ips,"ipconfig")