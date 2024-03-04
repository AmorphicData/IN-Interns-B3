#!bin/bash
if !aws --version &> /dev/null;then
    echo "AWS CLI is not installed. Please Install it Before Running"
    exit 1
fi

aws --version #aws version
read -p "Your Name:" name
flag=0
for profile in $(aws configure list-profiles --output text --query 'Profiles');
do
    if ["$profile"=="$name"];then
        flag=1
    fi
done
#Now for IAM Roles
echo "IAM Roles"
aws iam list-roles --profile $name --query "Roles[].RoleName" --output text

#Now 
echo "IAM roles starting with AWS"
aws iam list-roles  --profile $name --query "Roles[?starts_with(RoleName, 'AWS')].RoleName" --output text


#S3 Bucket
echo "S3 Bucket Names:"                                
aws s3api list-buckets --profile $name --query "Buckets[*].Name" --output text
