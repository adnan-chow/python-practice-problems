def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# Test the function
input_list = [1, [2, 3], [4, [5]]]
print(flatten_list(input_list))