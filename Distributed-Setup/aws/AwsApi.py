import boto3

def getPrivateIp(id):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=[id])
    ip = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
    return ip