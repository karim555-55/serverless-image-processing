# Deployment Instructions

## Prerequisites
- AWS account
- AWS CLI configured (optional)
- Basic understanding of AWS S3 and Lambda

## Steps
1. Create two S3 buckets:
   - `your-input-bucket-name`
   - `your-output-bucket-name`

2. Prepare Lambda Function:
   - Go to AWS Lambda console.
   - Create a new Lambda function (Python 3.9 or 3.10).
   - Create a new role with basic Lambda permissions.
   - Upload the provided `lambda_function.zip` file.

3. Install Dependencies:
   - Run `pip install -r requirements.txt -t .`
   - Create a ZIP file with all contents and upload to Lambda.

4. Add Trigger:
   - Add S3 trigger from the input bucket.
   - Event type: `PUT`

5. Test:
   - Upload an image to the input bucket.
   - Check the output bucket for the resized image.

