#Python program to remove duplicate words from a given string. Use the collections module
from collections import defaultdict

def remove_duplicate_words(input_string):
    words = input_string.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    unique_words = [word for word, count in word_counts.items() if count == 1]
    result_string = ' '.join(unique_words)
    return result_string


input_string = "hello world hello python world"
result = remove_duplicate_words(input_string)
print("Original String:", input_string)
print("String with Duplicate Words Removed:", result)
