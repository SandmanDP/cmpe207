import json
import boto3
from datetime import datetime
# That's the lambda handler, you can not modify this method
# the parameters from JSON body can be accessed like deviceId = event['deviceId']


def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    # 1 Parse out query string params
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionId=' + transactionId)
    print('transactionType=' + transactionType)
    print('transactionAmount=' + transactionAmount)

    # 2 Construct the body of the response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello from Lambda world'

    # 3 Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    # 4 Return the response object
    return responseObject
