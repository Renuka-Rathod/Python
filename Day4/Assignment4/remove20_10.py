"""list1 = [5, 20, 15, 20, 25, 50, 20]
output:
[5, 15, 25, 50]
"""
list1 = [5, 20, 15, 20, 25, 50, 20]
print("original list:",list1)

list1 = [x for x in list1 if x != 20]
print("Modified list:",list1)
