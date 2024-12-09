import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TASKS_TABLE', 'TasksTable')
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        # Get the taskId from the path parameters
        task_id = event['pathParameters']['id']

        # Parse the request body to get the new task data
        body = json.loads(event['body'])

        # Check if the 'task' field is present
        if "task" not in body:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing 'task' field in request body"})
            }

        # Update the task in the DynamoDB table
        response = table.update_item(
            Key={'taskId': task_id},
            UpdateExpression="set task = :task",
            ExpressionAttributeValues={':task': body['task']},
            ReturnValues="UPDATED_NEW"
        )

        # If the taskId doesn't exist, return a 404 error
        if response['Attributes'] is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": f"Task with taskId {task_id} not found"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"title":"Updated Task 1", "description":"This task has been updated", "status":"completed"})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
