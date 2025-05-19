def is_palindrome(word):
    # Normalize: lowercase and keep only letters
    normalized = ""
    for char in word.lower():
        if char.isalpha():
            normalized += char
    # Compare with its reverse
    return normalized == normalized[::-1]

# Test the function
input_word = "Madam"
print(is_palindrome(input_word))