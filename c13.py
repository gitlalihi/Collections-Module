#Python program to rotate a Deque Object a specified number (positive) of times.

import collections

dq_object = collections.deque()


dq_object.append(2)
dq_object.append(4)
dq_object.append(6)
dq_object.append(8)
dq_object.append(10)


print("Deque before rotation:")

print(dq_object)


dq_object.rotate()


print("\nDeque after 1 positive rotation:")


print(dq_object)


dq_object.rotate(2)


print("\nDeque after 2 positive rotations:")


print(dq_object) 
