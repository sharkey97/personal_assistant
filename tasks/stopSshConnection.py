import subprocess

def run(username):
    """Function to stop the SSH server on Windows and terminate active connections."""
    try:
        print("Stopping SSH server...")
        # Use subprocess to run PowerShell command to stop the SSH service with elevated permissions
        subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList", "'Stop-Service sshd'", "-Verb", "RunAs"], check=True)
        print("SSH server stopped successfully.")

        # Find and print any active SSH connections
        print("Checking for active SSH connections...")
        result = subprocess.run(["powershell", "-Command", "netstat -ano | findstr :22"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        
        connected_ips = set()  # Use a set to avoid duplicates
        if not lines:
            print("No active SSH connections found.")
        else:
            for line in lines:
                parts = line.split()
                if len(parts) >= 5:
                    local_address = parts[1]
                    remote_address = parts[2]
                    pid = parts[4]
                    
                    # Extract and print remote IP address (strip port if needed)
                    remote_ip = remote_address.split(':')[0]
                    connected_ips.add(remote_ip)
                    
                    # Check if the process is still running before attempting to kill it
                    try:
                        subprocess.run(["powershell", "-Command", f"Get-Process -Id {pid}"], check=True, capture_output=True, text=True)
                        subprocess.run(["taskkill", "/PID", pid, "/F"], check=True)
                        print(f"Terminated process with PID {pid}.")
                    except subprocess.CalledProcessError as e:
                        print(f"Failed to terminate process with PID {pid}: {e}. It may have already been closed.")

        if connected_ips:
            print("Active SSH connections from the following IP addresses:")
            for ip in connected_ips:
                print(ip)
        else:
            print("No active SSH connections found.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop SSH server: {e}")
