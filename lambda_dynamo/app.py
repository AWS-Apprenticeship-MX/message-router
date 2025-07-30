import json
import os
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MessagesTable')

def lambda_handler(event, context):
    print("Evento recibido desde SNS:", json.dumps(event))

    for record in event['Records']:
        sns_message = record['Sns']['Message']
        try:
            data = json.loads(sns_message)
            message = data.get("detail", {}).get("message", "Mensaje sin contenido")
        except Exception:
            message = sns_message

        table.put_item(
            Item={
                'MessageId': str(uuid.uuid4()),
                'Message': message
            }
        )

    return {
        "statusCode": 200,
        "body": json.dumps({"status": "Mensaje almacenado en DynamoDB"})
    }