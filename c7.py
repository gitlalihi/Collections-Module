#Python program to create a deque and append a few elements to the left and right. Next, remove some elements from the left and right sides and reverse the deque.
import collections 
deque_colors = collections.deque(["Red", "Green", "White"])
print(deque_colors)


print("\nAdding to the left: ")
deque_colors.appendleft("Pink")
print(deque_colors)

print("\nAdding to the right: ")
deque_colors.append("Orange")
print(deque_colors)


print("\nRemoving from the right: ")
deque_colors.pop()
print(deque_colors)


print("\nRemoving from the left: ")
deque_colors.popleft()
print(deque_colors)

print("\nReversing the deque: ")
deque_colors.reverse()
print(deque_colors) 
