#Python program to count the most and least common characters in a given
from collections import Counter

def count_characters(input_string):
    
    char_counts = Counter(input_string)

    
    most_common_char = char_counts.most_common(1)[0][0]

 
    least_common_char = char_counts.most_common()[:-2:-1][0][0]

    return most_common_char, least_common_char


input_string = "hello world"
most_common, least_common = count_characters(input_string)

print(f"Most common character: {most_common}")
print(f"Least common character: {least_common}")
