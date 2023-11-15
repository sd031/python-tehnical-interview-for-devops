import subprocess

def ping_server(server_ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", server_ip])
        return True
    except subprocess.CalledProcessError:
        return False

# Example usage
server_ip = '192.168.1.1'
if ping_server(server_ip):
    print(f"Server {server_ip} is reachable.")
else:
    print(f"Server {server_ip} is not reachable.")
