# Python program to count the number of times a specific element appears in a deque object.

import collections


nums = (2, 9, 0, 8, 2, 4, 0, 9, 2, 4, 8, 2, 0, 4, 2, 3, 4, 0)


nums_dq = collections.deque(nums)


print("Number of 2 in the sequence")


print(nums_dq.count(2))


print("Number of 4 in the sequence")


print(nums_dq.count(4)) 
