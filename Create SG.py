import boto3
from pprint import pprint
session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
client_obj=session.client(service_name='ec2',region_name='us-east-1')
resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')

vpc_id='vpc-07def5e85a7b039ea'
try:
    # #waiter = client_obj.get_waiter('security_group_exists')
    response = client_obj.create_security_group(
        Description='SG for aws project',
        GroupName='web-sg',
        VpcId=vpc_id)

    # waiter.wait(
    #     Filters=[
    #         {
    #             'Name': 'group-name',
    #             'Values': ['web_sg']
    #         }
    #     ])
    response_sg = client_obj.describe_security_groups(
        Filters=[
            {
                'Name': 'group-name',
                'Values': ['web_sg']
            }
        ]
    )
    pprint(response_sg)
    group_id = response_sg['SecurityGroups'][0]['GroupId']
    # #pprint(response_sg)
    print(group_id)


    client_obj.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/24',
                        'Description': 'SSH access from the users',
                    },
                ],
                'ToPort': 22,
            },],)
    client_obj.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
            {
                'FromPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/24',
                        'Description': 'Allow inbound https',
                    },
                ],
                'ToPort': 80,
            },],)
    client_obj.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
            {
                'FromPort': 443,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                    'CidrIp': '0.0.0.0/24',
                    'Description': 'allow inbound https',
                    },],
                'ToPort': 443,
        },],)
    client_obj.authorize_security_group_egress(
        GroupId=group_id,
        IpPermissions=[
            {
                'FromPort': 443,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '10.0.0.0/16',
                    },
                ],
                'ToPort': 443,
            },
        ],
    )

    print(response)
except Exception as e:
    print(e)