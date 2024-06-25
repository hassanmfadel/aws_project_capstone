import boto3
from pprint import pprint
session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
client_obj=session.client(service_name='ec2',region_name='us-east-1')
resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')
try:
    response = client_obj.run_instances(
    BlockDeviceMappings=[
        {       'Ebs': {
                'Encrypted': True
            },},],
    ImageId='ami-01b799c439fd5516a',
    InstanceType='t2.micro',
    KeyName='officekey',
    MaxCount=1,
    MinCount=1,
    Placement={
        'AvailabilityZone': 'us-east-1a'},
    SecurityGroupIds=[
        'sg-0403fa082a5493e4a',
    ],
    SubnetId='subnet-091f93a14605baca6',
    UserData='string')
    pprint(response)
except Exception as e:
    print(e)

