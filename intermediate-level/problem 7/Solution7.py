from collections import Counter
import re  # Added missing import

def top_ips(log_data):
    ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # Regex for IP address
    ips = []
    for line in log_data.splitlines():
        match = re.match(ip_pattern, line)
        if match:
            ips.append(match.group(0))
    return Counter(ips).most_common(3)

# Test the function (simulated log)
log_data = """192.168.1.1 - - [time] ...
192.168.1.2 - - [time] ...
192.168.1.1 - - [time] ...
192.168.1.3 - - [time] ...
192.168.1.1 - - [time] ..."""
print(top_ips(log_data))