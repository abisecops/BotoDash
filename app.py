from flask import Flask, render_template
import boto3
import pytz
from datetime import datetime

app = Flask(__name__)

# Initialize EC2 client
ec2 = boto3.client('ec2')

def get_instance_name(instance):
    """
    Retrieve the value associated with the 'Name' tag for an instance.
    If the tag is not found, return 'N/A'.
    """
    for tag in instance.get('Tags', []):
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'N/A'

@app.route('/')
def index():
    try:
        # Get information about all volumes
        volume_response = ec2.describe_volumes()
        volume_sizes = {}

        # Iterate over volumes and store volume ID and size in a dictionary
        for volume in volume_response['Volumes']:
            volume_id = volume['VolumeId']
            volume_size = volume['Size']
            volume_sizes[volume_id] = volume_size

        # Get information about all instances
        instance_response = ec2.describe_instances()
        instances = []

        # Iterate over instances to collect instance details
        for reservation in instance_response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_details = {
                    "Instance Type": instance['InstanceType'],
                    "State": instance['State']['Name'],
                    "Public IP Address": instance.get('PublicIpAddress', 'N/A'),
                    "Name": get_instance_name(instance),
                    "Launch Time": convert_to_indian_timezone(instance['LaunchTime'])
                }
                # Get the volume size for this instance
                for volume in instance.get('BlockDeviceMappings', []):
                    volume_id = volume['Ebs']['VolumeId']
                    instance_details["Volume Size"] = volume_sizes.get(volume_id, 'N/A')
                instances.append(instance_details)

        return render_template('index.html', instances=instances)

    except Exception as e:
        # Handle exceptions gracefully
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error_message=error_message)

def convert_to_indian_timezone(utc_time):
    # Convert UTC time to Indian timezone
    utc_time = utc_time.replace(tzinfo=pytz.utc)
    indian_timezone = pytz.timezone('Asia/Kolkata')
    indian_time = utc_time.astimezone(indian_timezone)
    return indian_time.strftime("%Y-%m-%d %I:%M:%S %p")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
