from __future__ import print_function
import os
import subprocess
import threading
from MasterHub import remoteExecution
from DisplayManager import printSuccess,printInfo,printFailure,printError
import sys
from SystemInformation import getSystemInformation,getPerfData
from Logger import logger
global jmeterPath
global reportPath
global gitPath
global executionType
global input_file
global timeout
global executionFlag
executionFlag = False
#sys.dont_write_bytecode = True



class JMeterExec():
    def __init__(self,jmeterPath, filepath,executionType,ExecutionParam=[]):
        getSystemInformation()
        global executionFlag
        os.chdir(jmeterPath)
        if ExecutionParam == []:
            try:
                executionFlag = True
                # starting thread 1
                printInfo("Executing Script : "+filepath)
                t1 = threading.Thread(target=getPerfData, args=())
                t1.start()
                #os.system("jmeter.bat -n -t"+ filepath)
                #output = subprocess.check_output("jmeter.bat -n -t"+ filepath, shell=True)
                #proc = subprocess.Popen(["jmeter.bat", "-n","-t", filepath], stdout=subprocess.PIPE, shell=True)
                logger.info("Starting JMeter")
                p = subprocess.Popen(["jmeter.bat", "-n","-t", filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output = p.stdout.read()
                filtered = lines = filter(lambda x: x.strip(), output)
                logger.info(filtered)
                #p.stdin.write(input)
                #(out, err) = proc.communicate()
                #print("program output:", out)
                executionFlag = False
                t1.join()
                printSuccess("Execution Complete")
            except:
                printFailure("FAILED")

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
                    t1 = threading.Thread(target=getPerfData, args=())

                    # starting thread 1
                    t1.start()
                    os.system("jmeter.bat -n -t "+ filepath+" -r -Gusers="+str(concurrency)+" -Grampup="+str(rampup)+" -Gcount="+str(iteration)+" -Gduration="+str(timeout)+" -GUrl="+str(url))
                    executionFlag = False
                    printSuccess("Execution Complete")
                except:
                    executionFlag = False
                    t1.join()
                    printFailure("FAILED")

            elif executionType == "masterhub":
                logger.info("Execution Started")
                remoteExecution("COMMAND::"+(" -r -Gusers=" + str(concurrency) + " -Grampup=" + str(rampup) + " -Gcount=" + str(iteration) + " -Gduration=" + str(timeout) + " -GUrl=" + str(url)))

            else:
                try:
                    executionFlag = True
                    t1 = threading.Thread(target=getPerfData, args=())
                    t1.start()
                    logger.info("Starting JMeter")
                    os.system("jmeter.bat -n -t " + filepath + " -Gusers=" + str(concurrency) + " -Grampup=" + str(rampup) + " -Gcount=" + str(iteration) + " -Gduration=" + str(timeout) + " -GUrl=" + str(url))
                    executionFlag = False
                    t1.join()
                    printSuccess("Execution Complete")

                except:
                    executionFlag = False
                    t1.join()
                    #printError(exe)
                    printFailure("FAILED")






