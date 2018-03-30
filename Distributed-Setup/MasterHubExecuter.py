from aws.CreateInstance import CreateAWSSetup
from aws.AwsApi import getPrivateIp
from RemoteExecution import ExecuteOnSystem
from JMeterExec import jmeter_execution
from colorama import Fore, Back, Style
import fileinput
import sys
import ReadInputFile
global gitPath
global jmeterPath
global executionType
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
            print(input_file)
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




def ConfigureExecution():
    ExecutionPara = ReadInputFile.GetExecutionParameters()

    timeout = ReadInputFile.GetTimeout()
    ExecutionPara['timeout'] = timeout

    JMXConfig = ReadInputFile.GetJMXSpecificConfig()
    ExecutionPara.update(JMXConfig)
    return ExecutionPara


class MasterHubExecuter():
    global gitPath
    global jmeterPath
    global executionType
    Config = ReadInputFile.GetConfigaration()
    gitPath = Config['gitPath']
    jmeterPath = Config['jmeterPath']
    #print(gitPath)
    Systems = CreateAWSSetup(gitPath)
    region = list(Systems.keys())
    for reg in region:
        ids = (Systems[reg])
        ips.append(getPrivateIp(ids[0]))
        del ips[0]

    print(ips)
    #for sys in Systems:
     #   print(Systems[sys])
        #ids = sys[list(sys.keys())[0]]
    input_file = InputFilePath()
    if "script" in input_file:
        script = input_file[1]
        executionType = "script"
        jmeter_execution(jmeterPath,script,executionType,[])


        ExecutionParameters = ConfigureExecution()
        #ExecutionParameters['ips'] = systems
        scripts = ExecutionParameters['scripts']
        del ExecutionParameters['scripts']
        print(ExecutionParameters)


        for script in scripts:
            filepath = gitPath + "/Scripts/Chrome/" + script
            PrintConfig("Script Execution", ExecutionParameters, filepath)
            #jmeter_execution(jmeterPath,filepath,executionType,ExecutionParameters)