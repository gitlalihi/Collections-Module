#Python program to count the most common words in a dictionary.
from collections import Counter

def count_most_common_words(word_dict):
    flattened_words = [word for words_list in word_dict.values() for word in words_list]
    word_counts = Counter(flattened_words)
    most_common_words = word_counts.most_common()
    return most_common_words


word_dictionary = {
    'group1': ['apple', 'banana', 'apple', 'orange'],
    'group2': ['apple', 'banana', 'grape', 'banana', 'grape']
}

result_most_common_words = count_most_common_words(word_dictionary)

print(result_most_common_words)
