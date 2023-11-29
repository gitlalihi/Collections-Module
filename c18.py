#Python program to find the item with the highest frequency in a given list.
from collections import Counter

def most_frequent_item(input_list):
    count_dict = Counter(input_list)
    most_common = count_dict.most_common(1)
    if most_common:
        most_frequent_element, frequency = most_common[0]
        return most_frequent_element, frequency
    else:
        return None, 0


input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
result, frequency = most_frequent_item(input_list)

if result is not None:
    print(f"The most frequent item is {result} with a frequency of {frequency}.")
else:
    print("The list is empty.")
