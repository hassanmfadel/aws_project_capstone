import boto3
from pprint import pprint




'''Create an IGW and Associate IGW to VPC'''
try:
    session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
    client_obj=session.client(service_name='ec2',region_name='us-east-1')
    resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')
    response = client_obj.create_internet_gateway()
    igw_ID = response['InternetGateway']['InternetGatewayId']
    vpc_ID = 'vpc-07def5e85a7b039ea'
    print(igw_ID)
    response2 = client_obj.attach_internet_gateway(InternetGatewayId=igw_ID, VpcId=vpc_ID)
    print(response2)

except Exception as e:
    print(e)

