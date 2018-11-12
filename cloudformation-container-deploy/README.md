##### Notes
- `aws ec2 describe-vpcs --query 'Vpcs[?IsDefault].VpcId' --output text` can get you your default VPC ID
-
    ```bash
    VPC_ID=$(aws ec2 describe-vpcs --query 'Vpcs[?IsDefault].VpcId' --output text)
    ```
-
    ```bash
    aws cloudformation deploy \
    --template-file cf.yml \
    --parameter-overrides $(cat parameters) \
    --stack-name test-cf
    ```
- `/var/log/cloud-init-output.log` inside EC2 instance has user data logs; very useful for debugging user data script