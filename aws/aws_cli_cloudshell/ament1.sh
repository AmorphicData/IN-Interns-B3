#!/bin/bash
if ! aws --version &> /dev/null; then
    echo "AWS CLI is not installed. Please install it before running this script."
    exit 1
fi
aws --version
read -p "Your Name:" name

check=0
#eq is for integer comparisons and double quotes are used if string contain any special characters or spaces
for profile in $(aws configure list-profiles --output text --query 'Profiles');
do
    if [ "$profile" == "$name" ];
     then
     $check=1
    fi
done
echo $check
echo "All IAM Roles:"                                   #List out all IAM roles
aws iam list-roles --profile $name --query "Roles[].RoleName" --output text
echo "IAM Roles starting with 'AWS':"                      #List of all IAM Roles starting with 'AWS'
aws iam list-roles --profile $name --query "Roles[?starts_with(RoleName, 'AWS')].RoleName" --output text

aws s3api list-buckets --profile $name --query "Buckets[*].Name" --output text


