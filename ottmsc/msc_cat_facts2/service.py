import json
# import boto3

def handler(event, context):
    # client = boto3.client('stepfunctions')
    # response = client.start_execution(
    #     stateMachineArn='arn:aws:states:us-east-2:164825194737:stateMachine:MyMscCatStateMachine',
    #     input=json.dumps(event)
    # )
    return {
        "message": "Wonderful! This is a cat fact 2!",
        "event": event
    }
