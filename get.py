import json
import boto3
import os
import requests
import json
from boto3.dynamodb.conditions import Key, Attr
import urllib

dynamodb = boto3.client('dynamodb', region_name= 'eu-west-1')
dynamodb_recource = boto3.resource('dynamodb', region_name='eu-west-1')


def getMessages(event, context):
    data = event['query']
    messages = data['receiver']

    table = dynamodb_recource.Table('ystavat-loppuprojekti-5-dev-ystavadynamodb-7S7RK6E6WA73')
    fe = Key('receiver').eq(messages)
    pe = "sender, content"
    response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe
    )
    print(response)
    return response['Items']
    
