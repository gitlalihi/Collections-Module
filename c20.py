#Python program to insert an element at the beginning of a given Ordered Dictionary.
from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
     new_dict = OrderedDict([(key, value)])
     new_dict.update(ordered_dict)
     return new_dict


ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

new_key = 'x'
new_value = 10

result_dict = insert_at_beginning(ordered_dict, new_key, new_value)

print("Original OrderedDict:", ordered_dict)
print("Modified OrderedDict:", result_dict)
