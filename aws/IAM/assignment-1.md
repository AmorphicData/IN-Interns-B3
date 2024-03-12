## IAM Assignment
----

Provide IAM policies / statements for the following scenarios:

1. **Restrict S3 Bucket Access to Specific EC2 Instance:**
   - Design an IAM policy that allows read and write access to a specific S3 bucket only from a designated EC2 instance. Ensure that no other instances can access the S3 bucket.

2. **Deny All EC2 Actions Except Run Instance:**
   - Create an IAM policy statement that denies all actions on EC2 except for the "RunInstances" action. Ensure that the policy allows users to launch EC2 instances while restricting other actions.

3. **Deny Actions Outside of us-east-1 Region:**
   - Craft an IAM policy statement that denies any AWS actions if they are not performed within the "us-east-1" region. Ensure the policy is effective in preventing users from executing actions in other regions.

4. **Enforce Tagging for Resources:**
   - Develop an IAM policy statement that enforces users to provide at least one tag for each resource they create across all AWS services. The policy should deny resource creation if the required tag is not provided.

5. **Allow Limited Access to EC2 Instances Based on Tags:**
   - Create an IAM policy that allows users to perform specific actions on EC2 instances based on tags. For example, grant users the ability to start and stop instances with a "Environment: Development" tag.

6. **Grant S3 Read-Only Access for a Specific IAM User:**
   - Design an IAM policy that grants read-only access to a specific S3 bucket for a particular IAM user. Ensure that the user cannot perform any write or delete actions on the specified S3 bucket.

7. **Implement Time-Based Access Control:**
   - Develop an IAM policy that allows certain actions only during specific time windows. For instance, permit users to terminate EC2 instances only during non-business hours.

8. **Conditional Access Based on IP Address:**
   - Craft an IAM policy statement that allows or denies access to AWS resources based on the IP address range of the requesting entity. For example, permit access only from a corporate network.

9. **Role Assumption with MFA:**
   - Create an IAM role with a trust relationship that allows users to assume the role only if multi-factor authentication (MFA) is enabled. Ensure that the policy requires MFA for successful role assumption.

10. **IAM Policy for Cross-Account Access:**
    - Design an IAM policy statement that allows cross-account access to specific resources. Specify the conditions under which the cross-account access is permitted.
