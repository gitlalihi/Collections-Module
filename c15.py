#Python program to find the majority element from a given array of size n using the Collections module.
from collections import Counter

def find_majority_element(arr):
    element_counts = Counter(arr)
    majority_element, count = element_counts.most_common(1)[0]
    if count > len(arr) / 2:
        return majority_element
    else:
        return None


arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = find_majority_element(arr)

if result is not None:
    print(f"The majority element is: {result}")
else:
    print("No majority element found.")
