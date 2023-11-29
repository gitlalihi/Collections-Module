# Python program to get the frequency of the tuples in a given list.
from collections import Counter

def tuple_frequency(input_list):
    frequency_counter = Counter(input_list)
    for tuple_item, frequency in frequency_counter.items():
        print(f'Tuple: {tuple_item}, Frequency: {frequency}')


input_list = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
tuple_frequency(input_list)
