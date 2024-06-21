import boto3
from pprint import pprint
session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
client_obj=session.client(service_name='ec2',region_name='us-east-1')
resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')
'''step2 create public subnets'''

response1 = client_obj.create_subnet(
    AvailabilityZone='us-east-1a',
    CidrBlock='10.0.10.0/24',
    VpcId='vpc-07def5e85a7b039ea')
response2 = client_obj.create_subnet(
    AvailabilityZone='us-east-1b',
    CidrBlock='10.0.20.0/24',
    VpcId='vpc-07def5e85a7b039ea')
pprint(response1)
pprint(response2)

