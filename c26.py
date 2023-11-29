#Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Use the collections module.
from collections import defaultdict

def group_key_value_pairs(key_value_pairs):
    grouped_dict = defaultdict(list)

    for key, value in key_value_pairs:
        grouped_dict[key].append(value)

    return dict(grouped_dict)


key_value_pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]

result_dict = group_key_value_pairs(key_value_pairs)

print(result_dict)
