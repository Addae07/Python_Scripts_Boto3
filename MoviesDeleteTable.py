import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-')

table = dynamodb.Table('Movies')

table.delete()
