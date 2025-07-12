import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    output_bucket = 'your-output-bucket-name'

    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    image_content = response['Body'].read()

    image = Image.open(io.BytesIO(image_content))
    image = image.resize((200, 200))

    output_buffer = io.BytesIO()
    image.save(output_buffer, format='JPEG')
    output_buffer.seek(0)

    s3.put_object(Bucket=output_bucket, Key=source_key, Body=output_buffer, ContentType='image/jpeg')

    return {'statusCode': 200, 'body': 'Image processed'}
