import fileinput
import sys
import argparse
from RemoteExecution import ExecuteOnSystem
from JMeterExec import JMeterExec as jmeter_executer
from DisplayManager import printWarning,printConfig,printSuccess,printInfo,printFailure
from Logger import logger
from MasterHub import checkStatus,executeCommand
import ReadInputFile
global gitPath
global jmeterPath
global executionType
executionType = "single"



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
    ips = []
    executionType = "masterhub"
    systems = ReadInputFile.GetMasterHubInfo()
    for key, value in systems.items():
        #print(key, value)
        if checkStatus(key):
            printInfo("Connected to "+ key)
            ip = ", ".join(value)
            logger.info(ip)
            #for ip in value:
                #print(ip)
            executeCommand(key,"EDIT::"+str(ip))

        ips.append(key)
    return ips

def copyFileToClient(ips,script):
    for ip in ips:
        with open(script, "rb") as f:
            data = f.read()
            executeCommand(ip,data)

def ConfigureExecution():
    ExecutionPara = ReadInputFile.GetExecutionParameters()


    timeout = ReadInputFile.GetTimeout()
    ExecutionPara['timeout'] = timeout

    JMXConfig = ReadInputFile.GetJMXSpecificConfig()
    ExecutionPara.update(JMXConfig)
    return ExecutionPara


def configSetup():
    global gitPath
    global jmeterPath
    global executionType
    printSuccess("Starting execution")
    printInfo("Configaration is taken from Default Input file")
    Config = ReadInputFile.GetConfigaration()
    gitPath = Config['gitPath']
    jmeterPath = Config['jmeterPath']
    logger.info("JMeter Path : " + jmeterPath)
    logger.info("Git Repository Path : " + gitPath)
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", help="Script to Execute")
    parser.add_argument("--input", help="Input file for Execution")
    args = parser.parse_args()
    if (args.script):
        script = args.script
        logger.info("Script Execution : " + script)
        executionType = "script"
        jmeter_executer(jmeterPath, script, executionType)

    elif (args.input):
        input_file = args.input
        logger.info("Input file : " + input_file)



    else:
        printWarning("No Input file given, trying to execute default Input file")
        input_file = "/Input/Input.yaml"
        input_file = gitPath + input_file
        logger.info("Input file : " + input_file)

    ReadInputFile.ReadUserInputFile(input_file)
    ExecutionParameters = ConfigureExecution()
    scripts = ExecutionParameters['scripts']
    logger.info(scripts)
    del ExecutionParameters['scripts']
    systems = []
    executionType = ReadInputFile.getExecutionType()
    if "masterhub" in executionType:
        systems = ConfigMasterDistributedSetup()
        logger.info("IP : "+str(systems))
        ExecutionParameters['ips'] = systems
        #checkConnection(systems)

    if "distributed" in executionType:
        print(executionType)


    #print(ExecutionParameters)


    for script in scripts:
            filepath = gitPath + "/Scripts/Chrome/" + script
            copyFileToClient(systems,filepath)
            printConfig("Script Execution",jmeterPath, ExecutionParameters, filepath)
            jmeter_executer(jmeterPath,filepath,executionType,ExecutionParameters)



class ExecuteSetup():
    try:
        #print("Started Configaring")
        configSetup()

    except KeyboardInterrupt:
        printFailure("FAILED")
        sys.exit()


