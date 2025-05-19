import csv
from io import StringIO

def top_users(csv_data):
    reader = csv.DictReader(StringIO(csv_data))
    users = [(row["name"], int(row["score"])) for row in reader]
    return sorted(users, key=lambda x: x[1], reverse=True)[:5]

# Test the function (simulated CSV)
csv_data = """name,score
Alice,90
Bob,85
Charlie,95
David,80
Eve,88"""
print(top_users(csv_data))