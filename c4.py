#Python program to find the occurrences of the 10 most common words in a given text.
from collections import Counter

def remove_punctuation(text):
    punctuation_chars = set(".,?!:;()[]{}'\"")
    cleaned_text = ''.join(char.lower() if char not in punctuation_chars else ' ' for char in text)
    return cleaned_text

def get_most_common_words(text, n=10):
    
    cleaned_text = remove_punctuation(text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(n)
    return most_common_words

if __name__ == "__main__":
    input_text = """
    This is an example text. You can replace it with your own text for testing.
    The goal is to find the occurrences of the 10 most common words in the given text.
    """
    most_common_words = get_most_common_words(input_text)
    print("The 10 most common words are:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
