import boto3

client = boto3.client('s3', 'east-us-1')

response = client.list_buckets()

print(response)