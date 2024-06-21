import boto3
from pprint import pprint
session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
client_obj=session.client(service_name='ec2',region_name='us-east-1')
resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')
'''step1 create a project_vpc vpc'''
try:
    response = client_obj.create_vpc(
        CidrBlock='10.0.0.0/16',
        #Ipv4NetmaskLength=16,
        #tagSpecifications=[{'Tags':[{'Key': 'Name','Value':'project_vpc'}]}]
    )
    print(response)
except Exception as e:
    print(e)