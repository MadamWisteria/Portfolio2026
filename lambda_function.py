import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('kiara-portfolio-stats')

def lambda_handler(event, context):
    # This magic 'update_item' call increments the number by 1 atomically
    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='ADD visitor_count :inc',
        ExpressionAttributeValues={':inc': 1},
        ReturnValues="UPDATED_NEW"
    )
    
    # Extract the new value
    new_count = response['Attributes']['visitor_count']
    
    # Return a friendly response to your JavaScript
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # This stops CORS errors!
            'Access-Control-Allow-Methods': 'GET',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': int(new_count)})
    }