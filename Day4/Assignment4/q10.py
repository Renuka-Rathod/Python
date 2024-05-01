"""10. Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
output:
[5, 15, 25, 50]"""
# Given list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all occurrences of 20 from the list using list comprehension
list1 = [x for x in list1 if x != 20]

# Print the modified list
print(list1)
