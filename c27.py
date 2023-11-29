#Python program to get the frequency of elements in a given list of lists. Use the collections module.
from collections import Counter

def count_element_frequency(list_of_lists):
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    element_frequency = Counter(flattened_list)
    return element_frequency


list_of_lists = [[1, 2, 3], [2, 3, 4], [1, 2, 3, 4, 5]]

result_frequency = count_element_frequency(list_of_lists)

print(result_frequency)
