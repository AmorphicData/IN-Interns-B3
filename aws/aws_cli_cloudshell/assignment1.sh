#!/bin/bash

if !aws --version &> /dev/null;then
    echo "AWS CLI is not installed. Please Install it Before Running"
    exit 1
fi

echo "AWS CLI version:"
aws --version

read -p “Enter your name:" user

if ! aws configure get profile.$user &> /dev/null; then
    echo "Error: AWS profile with the name is not set."
    exit 1
fi

echo "IAM Roles:"
aws iam list-roles --profile $user | jq -r '.Roles[].RoleName'

echo "IAM Roles starting with 'AWS':"
aws iam list-roles --profile $user | jq -r '.Roles[].RoleName' | grep '^AWS'

# S3 bucket names
echo "S3 Bucket names:"
aws s3api list-buckets --profile $user | jq -r '.Buckets[].Name'
