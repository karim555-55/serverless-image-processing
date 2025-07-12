# Serverless Image Processing using AWS Lambda and S3

## Overview
This project uses AWS Lambda and S3 to automatically process images when uploaded to an input S3 bucket. The image is resized and stored in an output bucket.

## Architecture
![Architecture Diagram](A_flowchart_diagram_illustrates_a_serverless_image.png)

## How It Works
1. User uploads an image to the S3 input bucket.
2. Lambda function is triggered automatically.
3. The function resizes the image.
4. The resized image is stored in a separate S3 output bucket.

## Tech Stack
- AWS S3
- AWS Lambda
- Python
- Pillow

## Setup Instructions
1. Create two S3 buckets: one for input and one for output.
2. Deploy the Lambda function using the provided code.
3. Add a trigger from the input bucket.
4. Upload images to test.

## Author
karim Alaa
