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

        # Delete the item from the DynamoDB table
        response = table.delete_item(Key={'taskId': task_id})

        # If the item was not found, return a 404 error
        if 'Attributes' not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": f"Task with taskId {task_id} not found"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"message": f"Task {task_id} deleted successfully"})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
