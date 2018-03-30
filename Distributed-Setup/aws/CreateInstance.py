import boto3
import yaml
import time
import os.path
import sys
import boto3
import os.path
import time

dirname, filename = os.path.split(os.path.abspath(__file__))
List = []

def PrintConfig(image, security, instanceNo, instType, region, subnet):
    print("*********** Creating Instance in "+region+" **************")
    print("image-id                                    :" + image)
    print("security-group-id                           :" + security)
    print("number-of-instance                          :" + str(instanceNo))
    print("type-of-instance                            :" + str(instType))
    print("region                                      :" + str(region))
    print("subnet-id                                   :" + str(subnet))
    print("************************************************")


def PrintResult(result, info):
    print("@@@@@@@@@@@@@@ " + result + " @@@@@@@@@@@@@@@@@@@@")
    print(info)


def CreateAWSSetup():
    global dirname
    ids = []
    if os.path.isfile("scale_up_infra/Input/aws-config.yaml"):
        # print("Reading the Input file...")
        with open("scale_up_infra/Input/aws-config.yaml", 'r') as stream:
            try:
                content = yaml.load(stream)
                regionVar = content['region']
                for region in regionVar:
                    sg = []
                    image = region['image-id']
                    instanceType = region['instance-type']
                    subnet = region['subnet']
                    instanceNo = region['instance']
                    security = region['security-group-id']
                    keyname = region['keyname']
                    region = region['name']


                    sg.append(security)
                    PrintConfig(image, security, instanceNo, instanceType, region, subnet)

                    try:
                        ec2 = boto3.resource('ec2', region_name=region)
                        subnet = ec2.Subnet(subnet)
                        instances = subnet.create_instances(ImageId=image, InstanceType=instanceType, MaxCount=instanceNo,
                                                            MinCount=instanceNo,
                                                            KeyName=keyname, SecurityGroups=[], SecurityGroupIds=sg)


                    except BaseException as exe:
                        PrintResult("Failure", exe)
                        sys.exit()

                    time.sleep(5)
                    for instance in instances:
                        id = instance.instance_id
                        ids.append(id)


                    List.append(ids[0])
                    del ids[0]
                    print(List,ids)

                if os.path.isfile(dirname + "\InstanceId.txt"):
                    file = open(dirname + "\InstanceId.txt", "w")
                    file.write('\n'.join(str(id) for id in ids))
                    file.close()
                    # print("Id has been written to file")
                    PrintResult("Success", instances)

                else:
                    print("InstanceId.txt file is not present in " + str(dirname) + "\InstanceId.txt")
                    sys.exit()

                if os.path.isfile(dirname + "\MasterId.txt"):
                    file = open(dirname + "\MasterId.txt", "w")
                    file.write('\n'.join(str(id) for id in List))
                    file.close()

                    # print("Id has been written to file")
                    PrintResult("Success", instances)



                else:
                    print("InstanceId.txt file is not present in " + str(dirname) + "\MasterId.txt")
                    sys.exit()

            except BaseException as exe:
                print("Problem in Input file 'aws-config.yaml'")
                PrintResult("Failure", exe)
                # print(exe)


    else:
        print("Fatal Error: Input file'aws-config.yaml' does not present in " + str(dirname) + "/aws-config.yaml")
        sys.exit()



    client = boto3.client('ec2')
    dirname, filename = os.path.split(os.path.abspath(__file__))

    print( "-------------------------------------------------")

    response = client.describe_instance_status(
        InstanceIds=ids
    )
    # print response

    for i in range(len(ids)):
        try:
            if response["InstanceStatuses"][i]:
                name = response["InstanceStatuses"][i]["InstanceState"]["Name"]
                id = response["InstanceStatuses"][i]["InstanceId"]
                while name != "running":
                    print("Instance state " + id + "," + name)

                    time.sleep(10)
                    name = response["InstanceStatuses"][i]["InstanceState"]["Name"]
                    response = client.describe_instance_status(InstanceIds=ids)

                print("Instance state " + id + "," + name)

                print("-------------------------------------------------")


        except BaseException as exe:
            print("Instance is terminated", exe)

    for i in range(len(ids)):
        try:
            if response["InstanceStatuses"][i]:
                status = response["InstanceStatuses"][i]["InstanceStatus"]["Status"]
                id = response["InstanceStatuses"][i]["InstanceId"]
                while status != "ok":
                    print("Instance Status Checks " + id + "," + status)

                    time.sleep(10)
                    status = response["InstanceStatuses"][i]["InstanceStatus"]["Status"]
                    response = client.describe_instance_status(InstanceIds=ids)

            print("Instance Status Checks " + id + "," + status)

            print("-------------------------------------------------")


        except BaseException as exe:
            print("Instance is terminated", exe)


    for i in range(len(ids)):
        try:
            if response["InstanceStatuses"][i]:
                systemStatus = response["InstanceStatuses"][i]["SystemStatus"]["Status"]
                id = response["InstanceStatuses"][i]["InstanceId"]
                while systemStatus != "ok":
                    print("System Status Checks " + id + "," + systemStatus)

                    time.sleep(10)
                    systemStatus = response["InstanceStatuses"][i]["SystemStatus"]["Status"]
                    response = client.describe_instance_status(InstanceIds=ids)

                print("System Status Checks " + id + "," + systemStatus)

                print("-------------------------------------------------")


        except BaseException as exe:
            print("Instance is terminated", exe)




CreateAWSSetup()