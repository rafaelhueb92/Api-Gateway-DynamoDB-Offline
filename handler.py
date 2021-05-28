import json
import boto3
import uuid

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event["body"]
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def put_user(event,context):

    body = json.loads(event["body"]);

    Id = str(uuid.uuid1())

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('usersTable')
    response = table.put_item(
       Item={
            'id': Id,
            'email':body["email"]
            }
    )

    return  {
        "statusCode": 200,
        "body": json.dumps({"id":Id})
    } 

def list_user(event,context):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('usersTable')
    response = table.scan()

    return  {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    } 

