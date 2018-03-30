# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import psutil
import json
import time
import platform
systemdict = {}
dict={}
systemdata = []
timedata = []

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

timeinfo = {}
systeminfo = {}
systeminfo['systeminfo'] = systemdict
systemdata.append(systeminfo)
for i in range(100):
    available_memory = psutil.virtual_memory().available
    total_memory = psutil.virtual_memory().total
    used_disk = psutil.disk_usage('/').used
    total_disk = psutil.disk_usage('/').total
    per_memeory = available_memory/total_memory*100
    per_disk = used_disk/total_disk*100
    dict['memory'] = per_memeory
    dict['disk'] = per_disk
    dict['time'] = time.ctime()
    timedata.append(dict)

timeinfo['timestamp'] = timedata
systemdata.append(timeinfo)
with open('C:/Users/Yajana/PycharmProjects/Distributed-setup-4/Data/data.json','w') as output:
    output.write(json.dumps(systemdata))
    #json.dumps(str_dict,output)



