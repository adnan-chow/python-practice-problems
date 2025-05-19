import re

def analyze_docker_log(log_data):
    pattern = r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+(ERROR|Exception):(.+)"
    errors = []
    for line in log_data.splitlines():
        match = re.match(pattern, line)
        if match:
            timestamp, error_type, message = match.groups()
            errors.append((timestamp, f"{error_type}: {message.strip()}"))
    return errors

# Test the function (simulated log)
log_data = """2023-10-01T12:00:00Z ERROR: Container failed to start
2023-10-01T12:01:00Z INFO: Running smoothly
2023-10-01T12:02:00Z Exception: Null pointer error"""
print(analyze_docker_log(log_data))