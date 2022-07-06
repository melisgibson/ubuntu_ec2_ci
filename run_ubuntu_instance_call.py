import os
from run_ubuntu_instance import *

client = boto3.client('ec2',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
    aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
)

create_apache_ec2(client, KeyName="private-ec2", SecurityGroups=["launch-wizard-6"])