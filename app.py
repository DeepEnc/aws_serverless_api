#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_serverless_api.aws_serverless_api_stack import AwsServerlessApiStack


app = cdk.App()
AwsServerlessApiStack(app, "AwsServerlessApiStack")

app.synth()
