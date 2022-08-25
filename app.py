#!/usr/bin/env python3
import aws_cdk as cdk

import constants
from database.infrastructure import RDSStack
from ecs.infrastructure import EcsCluster

app = cdk.App()

env = Environment(account = "090426658505", region = "ap-southeast-2")

rds_stack = RDSStack(
    app, "RDS-Stack", env=env)
ecs_stack = EcsCluster(
    app, "ECS-Stack", env=env)

ecs_stack.node.add_dependency(rds_stack)
# pipeline.node.add_dependency(ecs_stack)

app.synth()
