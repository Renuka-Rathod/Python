#10. Write a Python program to check if a set is a subset of another set.
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.issubset(s2) or s1 < s2)

s1 = { 4, 5}
s2 = {4, 5,6,7,8,9}
print(s1.issubset(s2) or s1 < s2)

