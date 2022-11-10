from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk.aws_ec2 as ec2

class AwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        self.vpc = ec2.Vpc(self, 'mainVPC', max_azs=2, # how many VPC object to use
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC, # controls Internet access, 
                name='public-subnet', # name this subnet group
                cidr_mask=24 # specifies the IP addresses in the range of individual subnets in the group
            )] )
