import boto3
import json


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Accounting')

    try:
        response = table.delete_item(
            Key={
                'transactionId': '1'
            },
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully deleted Transaction!')
        }

    except:
        print('Closing lambda function')
        return {
            'statusCode': 400,
            'body': json.dumps('Error deleting transaction')
        }
