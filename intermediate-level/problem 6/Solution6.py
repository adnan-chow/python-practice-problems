def flatten_json(nested, parent_key="", sep="."):
    flat = {}
    for key, value in nested.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flat.update(flatten_json(value, new_key, sep))
        else:
            flat[new_key] = value
    return flat

# Test the function
input_json = {"a": {"b": 1}}
print(flatten_json(input_json))