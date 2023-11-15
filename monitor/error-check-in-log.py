import re

def analyze_logs(file_path, pattern):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    error_lines = [line for line in logs if re.search(pattern, line)]
    return error_lines

# Example usage
log_file_path = '/path/to/logfile.log'
error_pattern = 'ERROR'
errors = analyze_logs(log_file_path, error_pattern)
for error in errors:
    print(error)
