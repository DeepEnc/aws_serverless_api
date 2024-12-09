from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    CfnOutput,
    Duration,
)
from constructs import Construct

class AwsServerlessApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB Table
        table = dynamodb.Table(
            self, "TasksTable",
            partition_key=dynamodb.Attribute(name="taskId", type=dynamodb.AttributeType.STRING)
        )

        # Lambda Functions
        create_task_function = _lambda.Function(
            self, "CreateTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="create_task.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TASKS_TABLE": table.table_name
            }
        )
        get_task_function = _lambda.Function(
            self, "GetTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="get_task.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TASKS_TABLE": table.table_name
            }
        )
        update_task_function = _lambda.Function(
            self, "UpdateTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="update_task.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TASKS_TABLE": table.table_name
            }
        )
        delete_task_function = _lambda.Function(
            self, "DeleteTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="delete_task.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TASKS_TABLE": table.table_name
            }
        )

        # Grant Lambda Functions access to DynamoDB
        table.grant_read_write_data(create_task_function)
        table.grant_read_write_data(get_task_function)
        table.grant_read_write_data(update_task_function)
        table.grant_read_write_data(delete_task_function)

        # API Gateway
        api = apigateway.RestApi(self, "TaskApi",
                                 rest_api_name="Task Service",
                                 description="This service manages tasks.")

        tasks = api.root.add_resource("tasks")

        # API Endpoints
        tasks.add_method("POST", apigateway.LambdaIntegration(create_task_function, timeout=Duration.seconds(29)))  # Create
        task = tasks.add_resource("{id}") 
        task.add_method("GET", apigateway.LambdaIntegration(get_task_function, timeout=Duration.seconds(29)))    # Read
        task.add_method("PUT", apigateway.LambdaIntegration(update_task_function, timeout=Duration.seconds(29)))   # Update
        task.add_method("DELETE", apigateway.LambdaIntegration(delete_task_function, timeout=Duration.seconds(29)))  # Delete
        
        CfnOutput(
            self, "ApiUrl",
            value=api.url,
            description="The URL of the Task API Gateway",
        )