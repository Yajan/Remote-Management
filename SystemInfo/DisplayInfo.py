from matplotlib import style
import time
style.use('ggplot')

import psutil



available_memory = psutil.virtual_memory().available
total_memory = psutil.virtual_memory().total
per = int(available_memory)/int(total_memory)*100
print(per)

total_disk = psutil.disk_usage('/').total
used_disk = psutil.disk_usage('/').used
disk = int(used_disk)/int(total_disk)*100
print(disk)

import matplotlib.pyplot as plt
#plt.axis([10,20,30,40,50,60,70,80,90,100])
plt.ion()
y = []
x= []
z= []

for i in range(100):
    plt.title("Memory and Disk")
    plt.xlabel("Started at "+time.ctime())

    available_memory = psutil.virtual_memory().available
    total_memory = psutil.virtual_memory().total
    per = int(available_memory) / int(total_memory) * 100

    total_disk = psutil.disk_usage('/').total
    used_disk = psutil.disk_usage('/').used
    disk = int(used_disk) / int(total_disk) * 100
    #print(disk)
    #plt.axis([0,i,1,100])
    y.append(per)
    x.append(i)
    z.append(disk)
    plt.plot(x,y)
    plt.plot(x,z)
    plt.pause(0.05)
    plt.show()

while True:
    plt.pause(0.05)




