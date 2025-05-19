def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    sentence = sentence.lower()
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# Test the function
input_sentence = "Data Science is awesome"
print(count_vowels(input_sentence))