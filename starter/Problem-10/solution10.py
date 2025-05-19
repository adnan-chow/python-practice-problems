data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
numbers_only = []

for item in data_list:
    if isinstance(item, (int, float)):
        numbers_only.append(item)

print(numbers_only)