def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

# Test the function
input_str = "bongodev"
print(reverse_string(input_str))