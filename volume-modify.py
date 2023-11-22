
import json
import boto3

def volume_id(volume_arn):
    vol = volume_arn.split("/")
    return vol[-1]

def lambda_handler(event, context):
    # Print the received event for debugging

    
        # Extract the volume ARN from the event
        volume_arn = event["resources"][0]
        
        # Create an EC2 client
        client = boto3.client('ec2')
        
        # Modify the volume type to 'gp3'
        response = client.modify_volume(
            VolumeId=volume_id(volume_arn),
            VolumeType='gp2'
        )
        
        # Return a response
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
  
