import boto3

def lambda_handler(event, context):
    # Connect to AWS
    ec2 = boto3.client('ec2')
    
    # Find running instances
    running = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    # Get instance IDs
    ids = []
    for r in running['Reservations']:
        for i in r['Instances']:
            ids.append(i['InstanceId'])
    
    # Stop them
    if ids:
        ec2.stop_instances(InstanceIds=ids)
        return f"Stopped {len(ids)} instances"
    
    return "No instances running"
