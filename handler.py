import json
import boto3
import os
from botocore.vendored import requests
from boto3.dynamodb.conditions import Key, Attr
import datetime

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
table = dynamodb.Table('ystavat-loppuprojekti-5-dev-ystavadynamodb-7S7RK6E6WA73')
CHARSET = 'UTF-8'

def saveYstavaQDB(content, sender, receiver):
    timestamp = str(datetime.datetime.now())
    response = table.put_item(
        Item={
            'sender': sender,
            'content': content,
            'receiver': receiver,
            'timestamp': timestamp
            }
    )


def sendEmail(event, context):
    data = event['body']
    sender = data ['sender']    
    source = data['source']    
    subject = data['subject']
    content = data['content']
    receiver = data['receiver']
    destination = data['destination']
    timestamp = datetime.datetime.now()


    _message = "Viesti kaveriltasi: " + sender + ": " + content + "."
    saveYstavaQDB(content, sender, receiver)
    client = boto3.client('ses' )    
        
    response = client.send_email(
        Destination={
            'ToAddresses': [destination]
            },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': _message,
                },
            },               
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source=source,
    )
    return _message
