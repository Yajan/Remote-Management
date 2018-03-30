import random
import os
import yaml
from colorama import Fore, Back, Style
global content
import sys

sys.dont_write_bytecode = True

def PrintError(exe):
    print(Fore.RED + "************** FAILED **************")
    print(Fore.RED+ exe)
    print(Style.RESET_ALL)


def GetConfigaration():
    global jmeterPath
    global gitPath
    global executionType
    global input_file
    with open("config/config.yaml", 'r') as stream:
        try:
            Config = {}
            content = yaml.load(stream)

            jmeterVar = content['jmeterPath']
            Config['jmeterPath'] = jmeterVar[0]

            gitVar = content['gitPath']
            Config['gitPath'] = gitVar[0]
            #print(gitPath)

            return Config


        except yaml.YAMLError as exc:
            PrintError(exc)

def GetTimeout():
    if "time-out" in content:
        timeout = content['time-out'][0]

        if (isinstance(timeout, int)):
            timeout = int(timeout) * 60
            return timeout

        elif "m" in timeout:
            timeout = timeout.replace("m", "")
            timeout = int(timeout) * 60
            return timeout

        elif "s" in timeout:
            timeout = timeout.replace("s", "")
            timeout = int(timeout)
            return timeout


def GetRemoteSystems():
    if "executionType" in content:
        executionContent = content['executionType']
        # print(executionContent)

        if 'distributed' in executionContent:
            executionVar = executionContent['distributed']
            # print(executionType)
            remoteSystemVar = executionVar['remote-systems']
            # print(remoteSystemVar)
            return remoteSystemVar


def GetExecutionParameters():
    executionConfig = {}
    if 'execution' in content:
        exection = content['execution']
        for var in exection:
            if "iteration" in var:
                executionConfig['iteration'] = var['iteration']
            elif "concurrency" in var:
                executionConfig['concurrency'] = var["concurrency"]
            elif "ramp-up" in var:
                rampup = var['ramp-up']

                if (isinstance(rampup, int)):
                    executionConfig['rampup'] = int(rampup)

                elif "m" in rampup:
                    rampup = rampup.replace("m", "")
                    executionConfig['rampup'] = int(rampup) * 60

                elif "s" in rampup:
                    rampup = rampup.replace("s", "")
                    executionConfig['rampup'] = int(rampup)
        return executionConfig

def GetJMXSpecificConfig():
    JMXConfig = {}
    if "url" in content:
        urlVar = content['url']
        JMXConfig['url'] = urlVar[0]

    if "random" in content:
        path = content['random'][0]
        lst = os.listdir(path)
        rand = random.randint(0, len(lst) - 1)
        JMXConfig['filepath'] = path + "\\" + lst[rand]
        return JMXConfig

    else:
        browsers = content['browsers']
        for browser in browsers:
            if "chrome" in browser:
                JMXConfig['browser'] = "chrome"

            elif "firefox" in browser:
                JMXConfig['browser'] = "firefox"

            scripts = content['scripts']
            JMXConfig['scripts'] = scripts

    return JMXConfig



def GetSystemConfig(groups):
    SystemInfo = {}
    with open('config/system.yaml', 'r') as stream:
        try:
            content = yaml.load(stream)
            for grp in groups:
                if "Windows" in content:
                    windowsSystem = content['Windows']
                    #print(windowsSystem)
                    systems = []
                    if grp in windowsSystem:
                        system_info = windowsSystem[grp]
                        for info in system_info:
                            info = info.split(",")
                            systems.append(info)

                        SystemInfo['windows'] = systems

                if "Linux" in content:
                    linuxSystem = content['Linux']
                    #print(linuxSystem)
                    systems = []
                    if grp in linuxSystem:
                        system_info = linuxSystem[grp]
                        for info in system_info:
                            info = info.split(",")
                            systems.append(info)

                        SystemInfo['linux'] = systems
                else:
                    print(grp + "is not present in system file")

            return SystemInfo

        except yaml.YAMLError as exc:
            print(exc)

def GetMasterHubInfo():
    SystemInfo = {}
    with open('config/system.yaml', 'r') as stream:
        try:
            content = yaml.load(stream)
            systems = content['masterhubs']
            return systems

        except yaml.YAMLError as exc:
            print(exc)


class ReadUserInputFile():
    def __init__(self, input_file):
        global content
        with open(input_file, 'r') as stream:

            try:
                content = yaml.load(stream)

            except yaml.YAMLError as exc:
                print(exc)