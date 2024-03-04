#!/bin/bash
#Author Name: Tarun Adhikari
#Publish Date: Mar 2, 2024
#Last Updated: Mar 3, 2024

if ! command -v aws &> /dev/null; then                  #Checks if awscli is present or not
    echo "AWS CLI not found!"
    exit 1
fi

aws_ver=$(aws --version | awk '{print $1" "$2}')        #Print cli version
echo "AWS CLI Version: $aws_ver"

profile_name="Tarun"
if ! aws configure get aws_access_key_id --profile $profile_name &> /dev/null; then              #Check if aws profile name is set or not
    echo "Error: AWS Profile name $profile_name not found."
    exit 1
fi

echo "All IAM Roles:"                                   #List out all IAM roles
aws iam list-roles --profile $profile_name --query "Roles[].RoleName" --output json

echo "IAM Roles starting with 'AWS':"                      #List of all IAM Roles starting with 'AWS'
aws iam list-roles --profile $profile_name --query "Roles[?starts_with(RoleName, 'AWS')].RoleName" --output json


echo "S3 Bucket Names:"                                 #List of all S3 Bucket Names
aws s3api list-buckets --profile $profile_name --query "Buckets[*].Name" --output json