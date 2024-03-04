#!/bin/bash

if ! aws --version &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install it and try again."
    exit 1
fi

aws --version

read -p "Name: " name

if ! aws configure get aws_access_key_id --profile ${name} &> /dev/null; then
    echo "Error: AWS profile with the name is not set."
    exit 1
fi


echo "Listing all IAM Roles:"
aws iam list-roles --profile ${name} | jq -r '.Roles[].RoleName'


echo "IAM Roles starting with 'AWS':"
aws iam list-roles --profile ${name} | jq -r '.Roles[].RoleName' | grep "^AWS"


echo "S3 bucket names:"
aws s3api list-buckets --query 'Buckets[].Name' --profile ${name} | jq -r '.[]'
