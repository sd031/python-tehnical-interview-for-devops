import psutil

def get_system_info():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, memory_usage, disk_usage

# Example usage
cpu, memory, disk = get_system_info()
print(f"CPU Usage: {cpu}%, Memory Usage: {memory}%, Disk Usage: {disk}%")
