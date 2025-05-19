from collections import Counter
import re

def most_frequent_word(text, stopwords):
    # Clean and normalize text
    words = re.findall(r"\b\w+\b", text.lower())
    # Filter out stopwords
    filtered_words = [word for word in words if word not in stopwords]
    # Count and find most frequent
    word_counts = Counter(filtered_words)
    return word_counts.most_common(1)[0][0]

# Test the function
input_text = "Machine learning is machine intelligence"
stopwords = ["is"]
print(most_frequent_word(input_text, stopwords))