#Python program that copies a deque object and verifies shallow copying.
from collections import deque
import copy
original_deque = deque([1, 2, 3, 4, 5])


shallow_copied_deque = copy.copy(original_deque)


original_deque.append(6)


print("Original deque:", original_deque)
print("Shallow copied deque:", shallow_copied_deque)
