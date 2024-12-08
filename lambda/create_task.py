import json
import boto3
import uuid
import os

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
# Fetch the table name dynamically from environment variables (recommended in production)
table_name = os.environ.get('TASKS_TABLE', 'TasksTable')
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        # Parse the incoming event body
        body = json.loads(event['body'])
        
        # Check if 'task' is in the body, and handle missing data
        if "task" not in body:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing 'task' field in request body"})
            }

        # Generate a new taskId
        task_id = str(uuid.uuid4())

        # Insert the task into the DynamoDB table
        table.put_item(Item={"taskId": task_id, "task": body["task"]})

        # Return a successful response
        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Task created successfully", "taskId": task_id})
        }

    except Exception as e:
        # Log any unexpected errors
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
