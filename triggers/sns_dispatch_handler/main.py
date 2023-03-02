import boto3
import json
import os

def handler(event,context):
    """Sample pure Lambda function"""
    state_machine_arn = os.environ['STATE_MACHINE_ARN']
    input_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    client = boto3.client('stepfunctions')
    sns_messages = []
    records = event["Records"]
    if records:
        for record in records:
            print(record["Sns"]["Message"])
            sns_messages.append(record["Sns"]["Message"])

    response = client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )

    return {
        "statusCode": 200,
        "body": sns_messages,
    }
