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

        # Retrieve the item from the DynamoDB table
        response = table.get_item(Key={'taskId': task_id})

        # If the item is not found, return a 404 error
        if 'Item' not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": f"Task with taskId {task_id} not found"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"taskId": task_id, "task": response['Item']['task']})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
