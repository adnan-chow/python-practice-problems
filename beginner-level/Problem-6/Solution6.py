def capitalize_words(sentence):
    words = sentence.split()
    capitalized = []
    for word in words:
        if word:
            capitalized.append(word[0].upper() + word[1:].lower())
        else:
            capitalized.append(word)
    return " ".join(capitalized)

# Test the function
input_sentence = "python for web developers"
print(capitalize_words(input_sentence))