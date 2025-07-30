import json
import boto3 # TODO EL ROLLO DE AWS
import os

eventbridge = boto3.client('events') # Maneja el event bridge

def lambda_handler(event, context):
    for record in event['Records']:
        message = record['body']
        print("Mensaje recibido: ", message)

        eventbridge.put_events(
            Entries=[
                {
                    'Source': 'my.sqs.processor',
                    'DetailType':'SQSMessage',
                    'Detail': json.dumps({'message': message}),
                    'EventBusName': 'MyCustomBus'
                }
            ]
        )

    return {"statusCode": 200, "body": "Mensajes enviados a EventBridge"}
