def find_duplicates(tags):
    seen = set()
    duplicates = set()
    for tag in tags:
        if tag in seen:
            duplicates.add(tag)
        else:
            seen.add(tag)
    return list(duplicates)

# Test the function
input_list = ["ai", "ml", "python", "ml", "dl", "ai"]
print(find_duplicates(input_list))