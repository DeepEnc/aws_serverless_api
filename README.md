
# SERVERLESS AWS API

A serverless CRUD API built using AWS Lambda, DynamoDB, API Gateway, and deployed with AWS CDK (Cloud Development Kit). This API allows you to perform CRUD operations (Create, Read, Update, Delete) on tasks.

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

2. Initialize the CDK App
```
cdk init app --language python
```
If you want to create everything from the beginning then perform this step on another directory and copy only remaining files from this repo. Else, this repo contains all the required CDK project structure. Hence, skip to next step. 

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Modify the stack in the below directory alc to the need or move on to the next step:
* `aws_serverless_api`
* `lambda`

5. Bootstrap CDK Environment
```
cdk bootstrap
```

6. Deploy the Stack
```
cdk deploy
```
After deployment is successful, the API Gateway URL will be provided in the output.

## Testing
Here, endpoints are tested using `curl`. However, tools like Postman can be used to test the endpoints.

1. Create a Task (POST/tasks):
```
url -X POST https://<api-gateway-url>/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Task 1", "description": "This is task 1"}'
```
where, `<api-gateway-url>` is the API GATEWAY URL value from the deploy step.
Also. `title` and `description` can be modified. The output consists of: `taskId`, `title`, `description`, and `status`

2. Get Task (GET/tasks/{taskId})
```
curl -X GET https://<api-gateway-url>/tasks/{id}
```
Here,  use the `taskId` from the previous step or any `taskId` if already present in the DynamoDB table.

3. Update task (PUT/tasks/{taskId})
```
curl -X PUT https://<api-gateway-url>/tasks/<taskId> \
-H "Content-Type: application/json" \
-d '{"title": "Task 1 Updated"}'
```
Here, Update the attributes: `title` and `description` alc to the needs. 

4. Delete task (DELETE/tasks/{taskId})
```
curl -X DELETE https://<api-gateway-url>/tasks/<taskId>
```
This will delete the taskId from the DynamoDB table.

## Cleanup
```
cdk destroy
```