rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
char_count = {}

for char in rhyme:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_frequent = max(char_count, key=char_count.get)
print(f"The most frequent character is '{most_frequent}' with {char_count[most_frequent]} occurrences")