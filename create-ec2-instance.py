#pip install boto3

# Configure your AWS credentials (typically located in ~/.aws/credentials):
# [default]
# aws_access_key_id = YOUR_ACCESS_KEY
# aws_secret_access_key = YOUR_SECRET_KEY

import boto3

def create_ec2_instance(image_id, instance_type, key_name, security_group):
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group]
    )
    return instances[0]

def main():
    # Example parameters - replace these with your desired values
    IMAGE_ID = 'ami-0abcdef1234567890'  # Example AMI ID
    INSTANCE_TYPE = 't2.micro'
    KEY_NAME = 'your-key-pair'
    SECURITY_GROUP = 'your-security-group-id'

    instance = create_ec2_instance(IMAGE_ID, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP)
    print(f"Instance created with ID: {instance.id}")

if __name__ == '__main__':
    main()
