import boto3
from pprint import pprint
session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
client_obj=session.client(service_name='ec2',region_name='us-east-1')
resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')



'''Create an IGW and Associate IGW to VPC'''
try:
    response = client_obj.create_internet_gateway()
    igw_ID = response['InternetGateway']['InternetGatewayId']
    vpc_ID = 'vpc-07def5e85a7b039ea'
    #print(igw_ID)
    response2 = client_obj.attach_internet_gateway(InternetGatewayId=igw_ID, VpcId=vpc_ID)
    #print(response2)
    '''let the route table in public subnets to route traffic through Internet Gateway'''
    rt_filter = [{'Name': 'tag:Name', 'Values': ['project_RT_public', ]}, ]
    public_rt_id = client_obj.describe_route_tables(Filters=rt_filter)['RouteTables'][0]['RouteTableId']
    route_table = resource_obj.RouteTable(public_rt_id)
    waiter = client_obj.get_waiter('internet_gateway_exists')
    waiter.wait(InternetGatewayIds=[igw_ID, ])
    route = route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_ID,LocalGatewayId=igw_ID)


except Exception as e:
    print(e)

