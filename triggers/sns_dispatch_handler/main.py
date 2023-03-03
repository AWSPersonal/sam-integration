import boto3
import json
import os


def handler(event, context):
    """Sample pure Lambda function"""
    state_machine_arn = os.environ['STATE_MACHINE_ARN']
    access_key = os.environ['ACCESS_KEY']
    secret_key = os.environ['SECRET_KEY']
    input_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    print("The ARN is ", state_machine_arn)
    client = boto3.client(
        'stepfunctions',
        aws_access_key_id=f"{access_key}",
        aws_secret_access_key=f"{secret_key}",)
    sns_messages = []
    records = event["Records"]
    if records:
        for record in records:
            print(record["Sns"]["Message"])
            sns_messages.append(record["Sns"]["Message"])

    client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )

    return {
        "statusCode": 200,
        "body": sns_messages,
    }
