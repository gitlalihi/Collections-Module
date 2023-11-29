#Python program to find the characters in a list of strings that occur more or less than a given number.
from collections import Counter

def find_characters(input_list, occurrence_threshold):
    
    all_characters = ''.join(input_list)

   
    char_counter = Counter(all_characters)

    
    more_than_threshold = [char for char, count in char_counter.items() if count > occurrence_threshold]

    
    less_than_threshold = [char for char, count in char_counter.items() if count < occurrence_threshold]

   
    print(f'Characters occurring more than {occurrence_threshold} times: {more_than_threshold}')
    print(f'Characters occurring less than {occurrence_threshold} times: {less_than_threshold}')


input_list = ['apple', 'banana', 'orange', 'grape']
occurrence_threshold = 2
find_characters(input_list, occurrence_threshold)
