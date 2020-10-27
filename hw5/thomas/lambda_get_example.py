import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    tableTransactions = dynamodb.Table('Transactions')

    response = tableTransactions.scan()

    return {
        'statusCode': 200,
        'body': response['Items']
    }
