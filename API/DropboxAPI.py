from __future__ import print_function

import requests
import json
ips = []
global jmeterPath
from os import listdir
from os.path import isfile, join
import socket
import requests
import json
global Auth_Token

def get_token():
    global Auth_Token
    with open("API",'r') as content:
        Auth_Token = content.read()
        print(Auth_Token)


def download_file(filepath):
    global Auth_Token
    url = "https://content.dropboxapi.com/2/files/download"

    headers = {
        "Authorization": Auth_Token,
        "Dropbox-API-Arg": "{\"path\":\""+filepath+"\"}"
    }

    r = requests.post(url, headers=headers)
    print(r)


def get_link(path):
    global Auth_Token
    url = "https://api.dropboxapi.com/2/sharing/create_shared_link"

    headers = {
        "Authorization": Auth_Token,
        "Content-Type": "application/json"
    }

    data = {
        "path": path
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))
    jsonurl = r.json()
    link = jsonurl['url']
    print(link)
    return link

def create_folder(foldername):
    global Auth_Token
    foldername="/"+str(foldername)
    url = "https://api.dropboxapi.com/2/files/create_folder"

    headers = {
        "Authorization": Auth_Token,
        "Content-Type": "application/json"
    }
    data = {
        "path": foldername
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print("Folder created")
    print(r.json())

def file_upload(filepath,filename,foldername):
    global Auth_Token
    foldername = "/"+str(foldername)
    filename = "/"+str(filename)

    url = "https://content.dropboxapi.com/2/files/alpha/upload"

    headers = {
        "Authorization": Auth_Token,
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": "{\"path\":\""+str(foldername)+str(filename)+"\"}"
    }

    data = open(filepath+filename, "rb").read()
    r = requests.post(url, headers=headers, data=data)
    print("File uploaded")
    print(r.json())







def store_data():
    testname = socket.gethostbyname(socket.gethostname())
    logpath = " C:/Users/Administrator/Documents/apache-jmeter-3.3/bin/TimestampsFolder"
    onlyfiles = [f for f in listdir(logpath) if isfile(join(logpath, f))]
    #print(onlyfiles)
    create_folder(testname)
    for file in onlyfiles:
        #print(file)
        file_upload(logpath,file,testname)
        #download_file("/10.0.1.35/jmeter-server.log")

#store_data()
get_token()
#download_file("/10.0.1.35/jmeter-server.log")










