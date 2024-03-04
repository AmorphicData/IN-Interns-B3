#!/bin/bash

# Validate if AWS CLI is installed
if ! aws --version &> /dev/null; then
    echo "AWS CLI is not installed. Please install it and try again."
    exit 1
fi

# Print AWS CLI version
aws --version

# Check if AWS profile is set
if [[ "$(aws configure get profile)" != "Ananya" ]]; then
    echo "AWS CLI profile is not set to Ananya. Please configure it using 'aws configure' and try again."
fi

# List all IAM Roles using above profile
echo "IAM Roles:"
aws iam list-roles --profile Ananya | jq -r '.Roles[].RoleName'

# Print IAM Roles starting with "AWS"
echo "IAM Roles starting with AWS:"
aws iam list-roles --profile Ananya --query "Roles[?starts_with(RoleName, 'AWS')].RoleName"

# Print S3 bucket names
echo "S3 Bucket Names:"
aws s3api list-buckets --query "Buckets[].Name"

