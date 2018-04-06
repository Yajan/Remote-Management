import socket
import threading
import time
from DisplayManager import printError,fatalError,printWarning,printInfo
from Logger import logger
ips = []
ips.append("")
global clientInfo
clientInfo = {}

def ConnectSlaves(ip):
   PORT = 8070
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect((ip, PORT))
   return client

def executeCommand(ip,command):
    logger.info(command)
    if ip in clientInfo:
       logger.info("Executing in "+ip)
       #logger.info(command)
       #print(command)
       client = clientInfo[ip]
       if type(command) is str:
            client.sendall((command).encode())
            in_data = client.recv(4096)
            #logger.info(ip+" : "+ in_data.decode())
            printInfo(ip+ ": "+in_data.decode())
       else:
           client.sendall(command)



def Listner(ip,duration):
    time.sleep(duration)
    try:
        client = clientInfo[ip]
        client.close()
    except:
        logger.info("Connection Closed")

def checkConnection(ips):
    max_try=3
    for ip in ips:
        for i in range(max_try):
            try:
                client = ConnectSlaves(ip)
                clientInfo[ip] = client
                break
            except:
                printError("Failed to connect for " + ip+ ": try "+str(i))
                time.sleep(0.1)

    if len(clientInfo) == 0:
        fatalError("No System got Connected, Nothing to execute")

def checkStatus(ip):
    max_try = 3
    for i in range(max_try):
        try:
            client = ConnectSlaves(ip)
            clientInfo[ip] = client
            return True
        except:
            printWarning("Failed to connect for " + ip + ": try " + str(i))
            time.sleep(0.1)
    printError("Unable to Connect to IP : "+ip)
    return False


def remoteExecution(commands):
    logger.info(commands)
    if clientInfo:
        for keys in clientInfo.keys():
            logger.info("Connected to "+ keys)
            t1 = threading.Thread(target=executeCommand, args=(keys, commands,))
            # t2 = threading.Thread(target=Listner,args=(keys,duration,))
            t1.start()
            # t2.start()



