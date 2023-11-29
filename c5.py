#Python program that accepts some words and counts the number of distinct words. Print the number of distinct words and the number of occurrences of each distinct word according to their appearance.
def count_distinct_words(words):
    word_count = {}
    distinct_words = []
    
    for word in words:
        if word not in word_count:
            word_count[word] = 1
            distinct_words.append(word)
        else:
            word_count[word] += 1
    
    return distinct_words, word_count

def main():
    input_words = input("Enter some words (separated by spaces): ").split()
    
    distinct_words, word_count = count_distinct_words(input_words)
    
    print("\nNumber of distinct words:", len(distinct_words))
    
    for word in distinct_words:
        print(f"{word}: {word_count[word]} occurrences")

if __name__ == "__main__":
    main()
