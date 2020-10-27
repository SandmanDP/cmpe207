import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Accounting')

    try:
        table.update_item(
            Key={
                'transactionId': '1'
            },
            UpdateExpression='SET transactionAmount = :val1',
            ExpressionAttributeValues={
                ':val1': 10000
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully updated Transaction!')
        }
    except:
        return {
            'statusCode': 400,
            'body': json.dumps('Error updating Transaction!')
        }
