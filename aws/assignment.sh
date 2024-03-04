#!/bin/bash

if ! aws --version &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install it and try again."
    exit 1
fi

aws --version

if ! aws configure get profile.${USER} &> /dev/null; then
    echo "Error: AWS profile with your name is not set. Please configure it and try again."
    exit 1
fi


echo "Listing all IAM Roles:"
aws iam list-roles --profile ${USER} | jq -r '.Roles[].RoleName'


echo "IAM Roles starting with 'AWS':"
aws iam list-roles --profile ${USER} | jq -r '.Roles[].RoleName' | grep "^AWS"


echo "S3 bucket names:"
aws s3api list-buckets --query 'Buckets[].Name' --profile ${USER} | jq -r '.[]'
