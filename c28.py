#Python program to count the occurrences of each element in a given list
from collections import Counter

def count_element_occurrences(input_list):
    element_occurrences = Counter(input_list)
    return element_occurrences


input_list = [1, 2, 3, 2, 1, 4, 5, 3, 6, 1, 2, 3]

result_occurrences = count_element_occurrences(input_list)

print(result_occurrences)
