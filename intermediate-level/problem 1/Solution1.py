def longest_word(sentence: str) -> str:
    words = sentence.split()                    # 1. tokenize
    return max(words, key=len)                  # 2. pick longest

print(longest_word("Machine learning is fascinating"))
# Output: fascinating