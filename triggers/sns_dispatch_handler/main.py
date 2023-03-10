import boto3
import json
import os


def handler(event, context):
    """Sample pure Lambda function"""
    state_machine_arn = 'arn:aws:states:ap-south-1:123456789012:stateMachine:SNS-Dispatcher'
    input_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    sns_messages = []
    records = event["Records"]
    if records:
        for record in records:
            print(record["Sns"]["Message"])
            sns_messages.append(record["Sns"]["Message"])
    client = boto3.client('stepfunctions', endpoint_url="http://{YOUR_PUBLIC_IP_ADDRESS}:8083")
    client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )
    print("VISIT THE STEP FUNCTIONS INITIATOR FOR FURTHER LOGS")
    return {
        "statusCode": 200,
        "body": sns_messages,
    }
