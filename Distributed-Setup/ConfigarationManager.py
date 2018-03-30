import MasterHub
from RemoteExecution import ExecuteOnSystem
from JMeterExec import jmeter_execution
from colorama import Fore, Back, Style
import fileinput
import sys
import ReadInputFile
global gitPath
global jmeterPath
global executionType
executionType = "single"
global ips
ips = []
def InputFilePath():
    if len(sys.argv) == 1:
        input_file = "/Input/Input.yaml"
        input_file = gitPath + input_file
        return input_file
    else:
        if "script" in sys.argv[1]:
            scriptVar = sys.argv[1]
            scriptArray = scriptVar.split("=")
            return scriptArray

        else:
            input_file = sys.argv[1]
            #print(input_file)
            return input_file

def PrintConfig(type,ExecutionPara,filepath):
    global jmeterPath
    print(Style.DIM+"************** "+type+" **************")
    print("jmeter-path              :"+jmeterPath)
    print("script                   :"+filepath)
    print("iteration-in-seconds     :"+str(ExecutionPara['iteration']))
    print("ramp-up-in-seconds:      :"+str(ExecutionPara['rampup']))
    print("concurrency              :"+str(ExecutionPara['concurrency']))
    print("time-out-in-seconds      :"+str(ExecutionPara['timeout']))
    print("browser                  :"+ExecutionPara['browser'])
    print("url                      :"+ExecutionPara['url'])
    print("systems-info             :"+str(ips))
    print("************************************************")
    print(Fore.GREEN + "************** Starting Execution **************")
    print(Style.RESET_ALL)

def read_n_write_ip(jmeterPath,ips):
    content = ", ".join(ips)
    text = "remote_hosts="
    x = fileinput.input(files=jmeterPath + "\jmeter.properties", inplace=1)
    for line in x:
        if text in line:
            line = "remote_hosts=" + content + "\n"
        sys.stdout.write(line)
    x.close()

def ConfigDistributedSetup(RemoteSys):
    global jmeterPath
    global executionType
    global ips
    SytemInfo = ReadInputFile.GetSystemConfig(RemoteSys)
    windowsInfo = SytemInfo['windows']
    for info in windowsInfo:
        ip = info[0]
        ips.append(ip)
        username = info[1]
        password = info[2]
        thread = ExecuteOnSystem(ip, username, password)
        thread.start()

    thread.join()
    read_n_write_ip(jmeterPath,ips)
    executionType = "distributed"


def ConfigMasterDistributedSetup():
    global executionType
    #print("Started")
    executionType = "masterhub"
    systems = ReadInputFile.GetMasterHubInfo()
    return systems



def ConfigureExecution():
    ExecutionPara = ReadInputFile.GetExecutionParameters()


    timeout = ReadInputFile.GetTimeout()
    ExecutionPara['timeout'] = timeout

    JMXConfig = ReadInputFile.GetJMXSpecificConfig()
    ExecutionPara.update(JMXConfig)
    return ExecutionPara


class ConfigarationManager():
    global gitPath
    global jmeterPath
    global executionType
    Config = ReadInputFile.GetConfigaration()
    gitPath = Config['gitPath']
    jmeterPath = Config['jmeterPath']
    input_file = InputFilePath()
    if "script" in input_file:
        script = input_file[1]
        executionType = "script"
        jmeter_execution(jmeterPath,script,executionType,[])

    else:
        ReadInputFile.ReadUserInputFile(input_file)
        ExecutionParameters = ConfigureExecution()
        if ReadInputFile.GetRemoteSystems():
            RemoteSys = ReadInputFile.GetRemoteSystems()
            #ConfigDistributedSetup(RemoteSys)
            systems = ConfigMasterDistributedSetup()
            #print(systems)
            ExecutionParameters['ips'] = systems

        scripts = ExecutionParameters['scripts']
        del ExecutionParameters['scripts']
        #print(ExecutionParameters)


        for script in scripts:
            filepath = gitPath + "/Scripts/Chrome/" + script
            PrintConfig("Script Execution", ExecutionParameters, filepath)
            jmeter_execution(jmeterPath,filepath,executionType,ExecutionParameters)







