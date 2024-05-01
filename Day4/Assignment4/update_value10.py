"""list1 = [5, 10, 15, 20, 25, 50, 20]
output:
list1 = [5, 10, 15, 200, 25, 50, 20]
"""
list1 = [5, 10, 15, 20, 25, 50, 20]
print("Original list:",list1)

index_20 = list1.index(20)
list1[index_20] = 200
print("Modified list",list1)
