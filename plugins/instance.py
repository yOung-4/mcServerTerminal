import boto3
import json
from plugins.config import get_config

ec2 = boto3.resource("ec2")


def get_state(id):
    response = ec2.describe_instance_status(
        InstanceIds=['i-0bd02f5a9b7423738',],)
    return response["InstanceStatuses"][0]["InstanceState"]["Name"]


def start_instance(id):
    instance = ec2.Instance(id)
    response = instance.start()
    return response["StartingInstances"][0]["CurrentState"]["Name"]


def stop_instance(id):
    instance = ec2.Instance(id)
    response = instance.stop()
    return response["StoppingInstances"][0]["CurrentState"]["Name"]
