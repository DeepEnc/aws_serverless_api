import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TASKS_TABLE', 'TasksTable')
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        task_id = event['pathParameters']['id']
        body = json.loads(event['body'])
        title = body.get('title')
        description = body.get('description')

        if not title or not description:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing 'title' or 'description' field in request body"})
            }

        response = table.update_item(
            Key={'taskId': task_id},
            UpdateExpression="set title = :title, description = :description",
            ExpressionAttributeValues={':title': title, ':description': description},
            ReturnValues="UPDATED_NEW"
        )

        if response['Attributes'] is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": f"Task with taskId {task_id} not found"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({
                "title": response['Attributes']['title'],
                "description": response['Attributes']['description'],
                "status": "completed"
            })
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
