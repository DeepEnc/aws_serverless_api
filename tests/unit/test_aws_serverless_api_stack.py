import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_serverless_api.aws_serverless_api_stack import AwsServerlessApiStack

def test_sqs_queue_created():
    app = core.App()
    stack = AwsServerlessApiStack(app, "aws-serverless-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
