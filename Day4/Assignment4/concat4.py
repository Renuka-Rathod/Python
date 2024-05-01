"""Print two lists in the following order
list1 = [5, 6,7]
list2 = [0, 1]
output:50,51,60,61,70,71
"""
list1 = [5, 6,7]
list2 = [0, 1]

list3 = [int(str(i)+str(j)) for i in list1 for j in list2]
print("method1:",list3)
l3=[]
for i in list1:
    for j in list2:
        l3.append(int(str(i)+str(j)))

print("method2:",l3)
