#Write a Python program to find the most common elements and their counts in a specified text

from collections import Counter
s = str(input("Enter your string:"))
print("Original string: " + s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3)) 
