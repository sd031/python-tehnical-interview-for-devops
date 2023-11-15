#pip install collections-extended

import re
from collections import Counter

def extract_ips(log_line):
    # Regular expression for matching and extracting IP addresses
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    match = re.search(ip_regex, log_line)
    if match:
        return match.group()
    return None

def count_ips(log_file_path):
    # Initialize a Counter object to count IP occurrences
    ip_counter = Counter()

    # Read the log file and count IP addresses
    with open(log_file_path, 'r') as file:
        for line in file:
            ip = extract_ips(line)
            if ip:
                ip_counter[ip] += 1

    return ip_counter

# Example usage
log_file_path = 'path/to/your/logfile.log'
ip_counts = count_ips(log_file_path)

# Display the 10 most common IP addresses
print("Most frequent IP addresses:")
for ip, count in ip_counts.most_common(10):
    print(f"{ip}: {count}")
