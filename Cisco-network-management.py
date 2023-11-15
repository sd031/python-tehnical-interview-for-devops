#pip install netmiko

from netmiko import ConnectHandler

# Network device configuration
device = {
    'device_type': 'cisco_ios',  # Adjust this based on your device
    'ip': '192.168.1.1',         # Device IP address
    'username': 'admin',         # Device login username
    'password': 'yourpassword',  # Device login password
}

# Command to execute
command = "show ip interface brief"

# Connect to the device
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command(command)
    print(output)
