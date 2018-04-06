import psutil
import time
import platform
from DisplayManager import printSysInfo
import JMeterExec
import json
global executionFlag
global systeminfo
systeminfo = {}
def getSystemInformation():
    global systeminfo

    systemdict = {}

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


    systeminfo['systeminfo'] = systemdict
    printSysInfo(systemdict)


def getPerfData():
    executionFlag = JMeterExec.executionFlag
    #print(executionFlag)
    timeinfo = {}
    dict={}
    total_memory = psutil.virtual_memory().total
    total_disk = psutil.disk_usage('/').total
    while executionFlag:
        available_memory = psutil.virtual_memory().available
        used_disk = psutil.disk_usage('/').used
        per_memeory = available_memory *100 /total_memory
        per_disk = used_disk *100 /total_disk
        dict['memory'] = per_memeory
        dict['disk'] = per_disk
        timeinfo[time.ctime()]=dict
        #printPerfData(dict)
        executionFlag = JMeterExec.executionFlag

    if not executionFlag:
        print(" ")
        global systeminfo
        systeminfo.update(timeinfo)
        with open('C:/Users/Yajana/PycharmProjects/Distributed-setup-4/Data/data.json','w') as output:
           output.write(json.dumps(systeminfo))
            #json.dumps(timeinfo,output)







