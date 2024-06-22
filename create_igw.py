import boto3
from pprint import pprint





try:
    session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
    client_obj=session.client(service_name='ec2',region_name='us-east-1')
    resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')
    response = client_obj.create_internet_gateway()
except Exception as e:
    print(e)
