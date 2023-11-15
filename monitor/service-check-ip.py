import socket

def check_service(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout of 1 second
    try:
        sock.connect((ip, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()

# Example usage
if check_service('192.168.1.1', 80):  # HTTP service check
    print("HTTP service is running.")
else:
    print("HTTP service is down.")
