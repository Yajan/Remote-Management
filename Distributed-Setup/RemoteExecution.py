import subprocess
from colorama import Fore, Back, Style
import threading
import sys
Invoke_Command_Script = "PowershellScripts/InvokeCommand1.ps1"
Copy_File_Script = "PowershellScripts/CopyFile1.ps1"




def Invoke_Command(server,username,password,command):
    try:
        p = subprocess.Popen(["powershell.exe ",Invoke_Command_Script,server,username,password,"-command",command], stdout=sys.stdout)

    except:
        print(Fore.RED,"************** Error in Connnecting "+server+" **************")


def Copy_File(server,username,password,frompath,topath):
    try:
        p = subprocess.Popen(["powershell.exe ",Copy_File_Script,server,username,password,frompath,topath],stdout=sys.stdout)
        p.communicate()

    except:
        print(Fore.RED,"************** Error in Connnecting "+server+" **************")


class ExecuteOnSystem(threading.Thread):
   def __init__(self, ip, username, password):
      sys.dont_write_bytecode = True
      threading.Thread.__init__(self)
      self.ip = ip
      self.username = username
      self.password = password
   def run(self):
      print("Starting " + self.ip)
      Invoke_Command(self.ip,self.username,self.password,"C:/slave.bat")
      print("Exiting " + self.ip)




class GetRemoteSystemInfo(threading.Thread):
   def __init__(self, ip, username, password):
      threading.Thread.__init__(self)
      global executionFlag
      self.ip = ip
      self.username = username
      self.password = password
   def run(self):
      print("Starting " + self.ip)
      while executionFlag:
        Invoke_Command(self.ip,self.username,self.password,"python C:/SystemInfo.py")

      print("Exiting " + self.ip)
