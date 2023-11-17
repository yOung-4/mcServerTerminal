import shutil
import os
import json


def get_config():
    file = open("config.json", "r")
    config = json.loads(file.read())
    return config


def set_aws_config():
    config = get_config()
    aws_access_key_id = config["auth"]["aws_access_key_id"]
    aws_secret_access_key = config["auth"]["aws_secret_access_key"]
    if os.path.exists(os.path.join(os.path.expanduser('~'), ".aws")):
        shutil.rmtree(os.path.join(os.path.expanduser('~'), ".aws"))
    os.mkdir(os.path.join(os.path.expanduser('~'), ".aws"))
    file = open(os.path.join(os.path.expanduser(
        '~'), ".aws/credentials"), "x")
    file.write(f'''
[default]
aws_access_key_id = {aws_access_key_id}
aws_secret_access_key = {aws_secret_access_key}
region = ap-east-1
               ''')
