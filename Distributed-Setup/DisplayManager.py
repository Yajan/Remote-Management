from __future__ import print_function
from colorama import Fore, Back, Style,init
import sys
from wcwidth import wcswidth
import shlex
import struct
import platform
import subprocess
import os
from Logger import logger



global sizex,sizey

""" getTerminalSize()
 - get width and height of console
 - works on linux,os x,windows,cygwin(windows)
"""
def get_terminal_size():
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        #print("default")
        tuple_xy = (80, 25)  # default value
    return tuple_xy


def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass


def _get_terminal_size_tput():
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])


def printSuccess(text):
    logger.info(text)
    global sizex
    text_len = wcswidth(text)
    side = int((sizex/2)-(text_len/2)-2)
    print(Fore.GREEN + u'*' * side, text, u'*' * side)
    print(Style.RESET_ALL)

def printFailure(text):
    #logger.warn(text)
    global sizex
    text_len = wcswidth(text)
    side = int((sizex/2)-(text_len/2)-2)
    print(Fore.RED + u'*' * side, text, u'*' * side)
    print(Style.RESET_ALL)

def onStart():
    logger.info("Display Setup Running")
    global sizex, sizey
    init(convert=True)
    #os.system('cls')
    sizex,sizey = get_terminal_size()

def printConfig(type,jmeterPath,ExecutionPara,filepath,ips=[]):
    printSuccess(type)
    logger.info("Execution Type : "+type)
    logger.info("Execution Parameters : "+str(ExecutionPara))
    print("jmeter-path              :"+jmeterPath)
    print("script                   :"+filepath)
    print("iteration-in-seconds     :"+str(ExecutionPara['iteration']))
    print("ramp-up-in-seconds:      :"+str(ExecutionPara['rampup']))
    print("concurrency              :"+str(ExecutionPara['concurrency']))
    print("time-out-in-seconds      :"+str(ExecutionPara['timeout']))
    print("browser                  :"+ExecutionPara['browser'])
    print("url                      :"+ExecutionPara['url'])
    print("systems-info             :"+str(ips))
    printSuccess("Starting Execution")
    print(Style.RESET_ALL)

def fatalError(error):
    error = str(error)
    printFailure("FAILED")
    print(Fore.RED+ error )
    logger.error(error)
    print(Style.RESET_ALL)
    sys.exit()

def printWarning(content):
    logger.warn(content)
    #print(Fore.YELLOW+ content)
    #print(Style.RESET_ALL)

def printInfo(content):
    logger.info(content)
    print(Fore.BLUE+content)
    print(Style.RESET_ALL)

def printError(exe):
    error = str(exe)
    #printFailure("FAILED")
    print(Fore.RED+ error)
    logger.error(error)
    print(Style.RESET_ALL)



def printSysInfo(dict):
    logger.info(dict)
    for var in dict:
        content = dict[var]
        print(Fore.BLUE+var,'=',content)
    print(Style.RESET_ALL)

# def printPerfData(dict):
#     #for var in dict:
#         #content = dict[var]
#     #sys.stdout.write("\r"  + "Time"+' = '+dict['time'] +" Disk" + ' = ' + str(dict['disk']) + " Memory"+ ' = '+str(dict['memory']))
#     #print("Time"+' = '+dict['time'] +" Disk" + ' = ' + str(dict['disk']) + " Memory"+ ' = '+str(dict['memory']))
#     logger.info("Time"+' = '+dict['time'] +" Disk" + ' = ' + str(dict['disk']) + " Memory"+ ' = '+str(dict['memory']))
#     #print("Hello world")
#     #sys.stdout.flush()

    #print(, end='\r')

class DisplayManager():
    onStart()













