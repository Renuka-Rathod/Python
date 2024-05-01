"""7. Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
        #0   1     2
# Access the nested list and append 7000
list1[2][2].append(7000)

# Print the modified list
print(list1)
