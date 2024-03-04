#!/bin/bash
# Step 1: Validate AWS CLI Installation
if !aws --version &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install it and try again."
    exit 1
fi
# Step 2: Print AWS CLI Version
aws --version
# Step 3: Check AWS Profile
profile_name="Harshini"  
if !aws configure get aws_access_key_id --profile "$profile_name" &> /dev/null; then
    echo "Error: AWS profile '$profile_name' is not set. Please configure it and try again."
    exit 1
fi
# Step 4: List IAM Roles
echo "IAM Roles associated with profile:"
aws iam list-roles --profile "$profile_name" --output text --query "Roles[*].RoleName"
# Step 5: Filter IAM Roles Starting with AWS
echo "IAM Roles starting with AWS:"
aws iam list-roles --profile "$profile_name" --output text --query "Roles[?starts_with(RoleName,'AWS')].RoleName"
# Step 6: List S3 Bucket Names
echo "S3 Bucket Names:"
aws s3api list-buckets --profile "$profile_name" --output text --query "Buckets[*].Name"
