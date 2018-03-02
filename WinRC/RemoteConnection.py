import subprocess, sys
import os
dirname, filename = os.path.split(os.path.abspath(__file__))
#print("running from", dirname)
#print("file is", filename)

Executer = "powershell.exe "
InvokeCommandScript = dirname+"/InvokeCommand "
CopyFileScript = dirname+"./CopyFile"
GetFileScript = dirname+"./GetFile"
RemoteSessionScript = dirname+"./RemoteSession"
StartRemoteSessionScript = dirname+"/StartRemoteSession"


def InvokeCommand(server,*therest):
    command = ', '.join(therest)
    p = subprocess.Popen([Executer,InvokeCommandScript,server,"-command",command], stdout=sys.stdout)
    p.communicate()


def ExecuteCommand(*therest):
    #print(list(therest))
    process = subprocess.Popen(list(therest), stdout=subprocess.PIPE)
    for line in process.stdout:
        sys.stdout.write(line)

def CopyFile(server,frompath,topath):
    p = subprocess.Popen([Executer,CopyFileScript,server,frompath,topath], stdout=sys.stdout)
    p.communicate()


def GetFile(server,frompath,topath):
    p = subprocess.Popen([Executer,GetFileScript, server, frompath, topath], stdout=sys.stdout)
    p.communicate()

def RemoteSession(server):
    p = subprocess.Popen("powershell "+RemoteSessionScript+" "+server)
    p.wait()
    #p = subprocess.Popen([Executer,RemoteSessionScript,server], stdout=sys.stdout)
    #p.communicate()

def StartRemoteSession(server):
    p = subprocess.Popen("powershell "+StartRemoteSessionScript+" "+server)
    p.wait()



def Credencials(host):
    global Username
    global Password
    global ip
    with open('.host/host', 'r') as f:
        #print(f.read())
        for line in f:
            #print(line)
            if host in line:
                for word in line.split():
                    #print(word)
                    if host in word:
                        server = word.split("=")
                        ip = server[1]


                    if "username" in word:
                        user = word.split("=")
                        Username=user[1]


                    if "password" in word:
                        passwd = word.split("=")
                        Password=passwd[1]

    #print(ip,Username,Password)



#InvokeCommand("server","cd","/")
#ExecuteCommand("netstat","-an")
#CopyFile("windows","C:/Distributed-setup/ipconfig.txt",'C:/Test')
#GetFile("windows",'C:/Test/ipconfig.txt',"C:/Test")