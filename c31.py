#Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
from collections import OrderedDict

def create_ordered_dict(input_dict):
    ordered_dict = OrderedDict(input_dict)
    return ordered_dict


input_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4}
ordered_dict = create_ordered_dict(input_dict)
for key, value in reversed(ordered_dict.items()):
    print(key, value)
