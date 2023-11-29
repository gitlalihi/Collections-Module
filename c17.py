#Python program to break a given list of integers into sets of a given positive number. Return true or false.
from collections import Counter

def break_into_sets(input_list, positive_number):
   if positive_number <= 0:
        return False
   count_dict = Counter(input_list)
   for count in count_dict:
        if count % positive_number != 0:
            return False
        return True


input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
positive_number = 3

result = break_into_sets(input_list, positive_number)

if result:
    print(f"It is possible to break the list into sets of {positive_number}.")
else:
    print(f"It is not possible to break the list into sets of {positive_number}.")
