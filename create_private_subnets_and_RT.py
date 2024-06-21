import boto3
from pprint import pprint
session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
client_obj=session.client(service_name='ec2',region_name='us-east-1')
resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')

'''step2 create private subnets'''
#waiter = client_obj.get_waiter('subnet_available')
subnet1 = client_obj.create_subnet(
    AvailabilityZone='us-east-1a',
    CidrBlock='10.0.100.0/24',
    VpcId='vpc-07def5e85a7b039ea')
subnet2 = client_obj.create_subnet(
    AvailabilityZone='us-east-1b',
    CidrBlock='10.0.200.0/24',
    VpcId='vpc-07def5e85a7b039ea')
private_subnet1_id=subnet1['Subnet']['SubnetId']
private_subnet2_id=subnet2['Subnet']['SubnetId']

#waiter.wait(Filters=[{'Name': 'tag:Name','Values':['private_subnet_1',]},])

'''create tag to each subnet'''
# client_obj.create_tags(
#     Resources=private_subnet1_id,
#     Tags=[{'Key': 'Name', 'Value': 'private_subnet_1'}]
# )
# client_obj.create_tags(
#     Resources=private_subnet2_id,
#     Tags=[{'Key': 'Name', 'Value': 'private_subnet_2'}]
# )

#[{'Name': 'tag:Name','Values':['centos',]},]
'''here must use waiter, to wait till the private subnet created then create route table then wait..then associate it '''
'''create a route table'''
route_table = client_obj.create_route_table(VpcId='vpc-07def5e85a7b039ea')
route_table_id=route_table['RouteTable']['RouteTableId']

'''associate the new route table with the private subnets'''
client_obj.associate_route_table(RouteTableId=route_table_id,
                                            SubnetId=private_subnet1_id)
client_obj.associate_route_table(RouteTableId=route_table_id,
                                            SubnetId=private_subnet2_id)

