import subprocess

def run(username):
    print("Executing: Port Scanner...")

    try:
        # Run the PowerShell command to get USB devices with status OK
        result = subprocess.run(
            ['powershell', '-Command', 'Get-PnpDevice -InstanceId "USB*" -Status OK | Select-Object -Property Status, Class, FriendlyName, InstanceId'],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Process the result to display it nicely
        if result.stdout:
            lines = result.stdout.strip().split('\n')
            headers = lines[0].split()
            data_lines = lines[2:]  # Skip header and separator line
            
            for line in data_lines:
                # Ensure that we split based on fixed-width fields considering spaces in FriendlyName
                fields = line.split(None, len(headers) - 1)
                device_info = dict(zip(headers, fields))
                
                status = device_info.get('Status', 'N/A')
                device_class = device_info.get('Class', 'N/A')
                friendly_name = device_info.get('FriendlyName', 'N/A')
                instance_id = device_info.get('InstanceId', 'N/A')
                
                print(f"Status: {status}")
                print(f"Class: {device_class}")
                print(f"Friendly Name: {friendly_name}")
                print(f"Instance ID: {instance_id}")
                print("-" * 40)
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")