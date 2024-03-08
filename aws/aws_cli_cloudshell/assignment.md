
# Write a shell script which does the following:

- Validates whether aws cli is installed, if not exit with the proper error message, if installed correcty go ahead with next steps.
- Prints the aws cli version
- Checks if aws profile with your name is set, if not exit with the proper error message, if yes - go ahead
- Run aws cli command using the above profile to list all IAM Roles and prints them
- Loop through all IAM Roles and prints the iam roles which starts with "AWS"
- Run the aws cli command using the above profile to print only the s3 bucket names.


Note: All of the above steps should happen within one single shell script.