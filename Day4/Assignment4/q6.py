"""6. Remove empty strings from the list of strings
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]
"""
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
for i in list1:
    if i=="":
        list1.remove(i)
print(list1)
