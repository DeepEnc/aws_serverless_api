import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TASKS_TABLE', 'TasksTable')
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        body = json.loads(event['body'])
        
        if "task" not in body:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing 'task' field in request body"})
            }

        # Generate a new taskId
        task_id = str(uuid.uuid4())
        title = body.get("title", "Task Title")
        description = body.get("description", "Task Description")
        status = "pending"

        table.put_item(Item={
            "taskId": task_id,
            "title": title,
            "description": description,
            # "task": body["task"], 
            "status": status})

        return {
            "statusCode": 201,
            "body": json.dumps({
                "taskId": task_id,
                "title": title,
                "description": description,
                # "task": body["task"],
                "status": status})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
