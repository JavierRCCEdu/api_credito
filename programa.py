import boto3
import json

#boto 3 permite conectarse a cualquier servicio de amazon

client = boto3.client('sagemaker-runtime', 'us-east-1')

response=client.invoke_endpoint(EndpointName="sagemaker-scikit-learn-2022-05-21-00-47-28-325", 
				Body=b'[[1,2,1,0]]')

result = json.loads(response['Body'].read().decode())

print(result)
