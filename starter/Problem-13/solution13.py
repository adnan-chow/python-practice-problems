dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_keys = list(set(dict1.keys()) & set(dict2.keys()))
print("Common keys:", common_keys)