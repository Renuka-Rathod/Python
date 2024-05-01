#9. Write a Python program to find repeated items in a tuple.

t1=(9,9,9,9,9,23,45,67,67,10)
#Method1two for loop
#Method2use count function t1.count(9)
#Method3 use set

#m3 using set
# for e1 in set(t1):
#     if t1.count(e1) > 1:
#         print("repeated elem",e1)

# repeated_set = {}
# for e1 in set(t1):
#     if t1.count(e1) >1:
#         print("repeated elem",e1)
repeated_set = set()
for idx1 in range(len(t1)):
    for idx2 in range(len(t1)):
        if(idx1 != idx2) and (t1[idx1] == t1[idx2] and t1[idx1] not in repeated_set):
            repeated_set.add(t1[idx1])
print(repeated_set)

