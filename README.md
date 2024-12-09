
# SERVERLESS AWS API PROJECT !

A serverless CRUD API built using AWS Lambda, DynamoDB, and API Gateway, and deployed with AWS CDK (Cloud Development Kit). This API allows you to perform CRUD operations (Create, Read, Update, Delete) on tasks.

## Requirements

* AWS CLI installed and configured.
* Node.js (for AWS CDK).
* Python 3.x (for Lambda function development).

## Installation
Install AWS CDK:
```
npm install -g aws-cdk
```
## Setup
1. Clone the repo
```
git clone git@github.com:DeepEnc/aws_serverless_api.git

cd aws_serverless_api
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Initialize the CDK App
```
cdk init app --language python
```
4. Modify the stack in the below directory or move on to the next step:
* `aws_serverless_api`
* `lambda`

4. Bootstrap CDK Environment
```
cdk bootstrap
```

5. Deploy the Stack
```
cdk deploy
```
After deployment is successful, the API Gateway URL will be provided in the output.

## Testing
Here, endpoints are tested using `curl`. However, tools like Postman can be used to test the endpoints.

1. Create a Task(POST/task):
```
url -X POST https://<api-gateway-url>/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Task 1", "description": "This is task 1"}'
```
where, `<api-gateway-url>` is the API GATEWAY URL value from the deploy step.
Also. `title` and `description` can be modified.

Enjoy!
