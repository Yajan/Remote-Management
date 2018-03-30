from __future__ import print_function
import os
from colorama import Fore, Back, Style
import threading
import psutil
import json
import time
import platform
import MasterHub
import DisplayManager
global jmeterPath
global reportPath
global gitPath
global executionType
global input_file
global timeout
global executionFlag
executionFlag = False
import sys

sys.dont_write_bytecode = True

class jmeter_execution():
    def __init__(self,jmeterPath, filepath,executionType,ExecutionParam):
        global executionFlag
        display = DisplayManager.displayContent()
        os.chdir(jmeterPath)
        if ExecutionParam == []:
            try:
                executionFlag = True
                t1 = threading.Thread(target=SystemInfo, args=())

                # starting thread 1
                t1.start()
                print(filepath)
                display.displayLeft(os.system("jmeter.bat -n -t"+ filepath))
                executionFlag = False
                t1.join()
                print(Fore.GREEN + "************** Execution Complete **************")
                print(Style.RESET_ALL)
            except:
                print(Fore.RED + "************** FAILED **************")
                print(Style.RESET_ALL)

        else:
            iteration = ExecutionParam['iteration']
            rampup = ExecutionParam['rampup']
            concurrency = ExecutionParam['concurrency']
            timeout = ExecutionParam['timeout']
            url = ExecutionParam['url']

            if "ips" in ExecutionParam:
                ips = ExecutionParam['ips']

            if executionType == "distributed":
                try:
                    executionFlag = True
                    t1 = threading.Thread(target=SystemInfo, args=())

                    # starting thread 1
                    t1.start()
                    display.displayLeft(os.system("jmeter.bat -n -t "+ filepath+" -r -Gusers="+str(concurrency)+" -Grampup="+str(rampup)+" -Gcount="+str(iteration)+" -Gduration="+str(timeout)+" -GUrl="+str(url)))
                    executionFlag = False
                    print(Fore.GREEN + "************** Execution Complete **************")
                except:
                    print(Fore.RED + "************** FAILED **************")
                    print(Style.RESET_ALL)

            elif executionType == "masterhub":
                MasterHub.RemoteSocketManager(ips,(jmeterPath+"\jmeter.bat -n -t " + filepath + " -r -Gusers=" + str(concurrency) + " -Grampup=" + str(rampup) + " -Gcount=" + str(iteration) + " -Gduration=" + str(timeout) + " -GUrl=" + str(url)))

            else:
                try:
                    executionFlag = True
                    t1 = threading.Thread(target=SystemInfo, args=())
                    t1.start()
                    display.displayLeft(os.system("jmeter.bat -n -t " + filepath + " -Gusers=" + str(concurrency) + " -Grampup=" + str(rampup) + " -Gcount=" + str(iteration) + " -Gduration=" + str(timeout) + " -GUrl=" + str(url)))

                    executionFlag = False
                    print(Fore.GREEN + "************** Execution Complete **************")
                    print(Style.RESET_ALL)

                except:
                    print(Fore.RED + "************** FAILED **************")
                    print(Style.RESET_ALL)


def SystemInfo():
    global executionFlag
    systemdict = {}
    dict = {}

    mechine = platform.machine()
    version = platform.version()
    platformname = platform.platform()
    name = platform.uname()
    system = platform.system()
    processor = platform.processor()

    systemdict['mechine'] = mechine
    systemdict['version'] = version
    systemdict['platform'] = platformname
    systemdict['name'] = name
    systemdict['system'] = system
    systemdict['processor'] = processor

    print(systemdict)
    while executionFlag:
        # The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
        # License: http://creativecommons.org/licenses/by-sa/3.0/

        available_memory = psutil.virtual_memory().available
        total_memory = psutil.virtual_memory().total
        used_disk = psutil.disk_usage('/').used
        total_disk = psutil.disk_usage('/').total
        per_memeory = available_memory / total_memory * 100
        per_disk = used_disk / total_disk * 100
        dict['memory'] = per_memeory
        dict['disk'] = per_disk
        dict['time'] = time.ctime()

        display = DisplayManager.displayContent()
        display.displayRight(str(dict))

    display.endSession()



