# import boto3
# from pprint import pprint
# session=boto3.session.Session(profile_name='iam-admin',region_name='us-east-1')
# client_obj=session.client(service_name='ec2',region_name='us-east-1')
# resource_obj=boto3.resource(service_name='ec2',region_name='us-east-1')
#
#
#
# try:
#     '''Reading the private subnet ID'''
#     rt_filter = [
#         {
#             'Name': 'route-table-id',
#             'Values': [
#                 'rtb-028f6e9fd388656b5',
#             ]
#         },
#     ]
#     rt = client_obj.describe_route_tables(Filters=rt_filter)
#     subnet_ids=[]
#     associated_subnets_with_rt=rt['RouteTables'][0]['Associations']
#     for subnet in associated_subnets_with_rt:
#         subnet_ids.append(subnet['SubnetId'])
#     print(f"list of subnets associated with RT: {subnet_ids}")
#     '''AllocationId= is Elastice ip ID'''
#     for id in subnet_ids:
#         client_obj.create_nat_gateway( AllocationId='eipalloc-008ee73bcf95aca1a',SubnetId=id)
# except Exception as e:
#     print(e)