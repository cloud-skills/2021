import json
import boto3
import logging
from botocore.exceptions import ClientError


def lambda_handler(event, context):
  try:
    user_text = event['text']
    aws_region = event['region']
    bucket_name = event['bucket']

    current_date = datetime.datetime
    target_name = current_date + '_log.txt'
    source_name = 'string.txt'

    client = boto3.client('s3', region_name=aws_region)
    client.create_bucket(Bucket=bucket_name)
    
    f = open(source_name, 'w')
    f.write(user_text)
    f.close()
    
    response = client.upload_file(source_name, bucket_name, target_name)
  except ClientError as e:
    logging.error(e)
  
  return 200