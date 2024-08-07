import subprocess
import socket

def get_ip_address():
    """Get the local IP address of the Windows machine."""
    try:
        # Create a socket connection to a public DNS server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external IP address and port
        s.connect(("8.8.8.8", 80))
        # Retrieve the local IP address from the socket connection
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return "Unable to determine IP address"

def run(username):
    """Function to start the SSH server on Windows."""
    try:
        print(f"Starting SSH server for {username}...")
        # Use subprocess to run PowerShell commands with elevated permissions
        # Note: This will prompt for elevation
        subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList", "'Start-Service sshd'", "-Verb", "RunAs"], check=True)
        print("SSH server started successfully.")
        
        # Get and print the IP address
        ip_address = get_ip_address()
        print(f"You can now connect via SSH using the following IP address: {ip_address}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start SSH server: {e}")

