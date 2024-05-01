"""23. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""
#if same value is repeat this logic will fail.

l=[('item1','l2.20'),('item2','15.10'), ('item3','24.5')]
l=[('1',1.2),('2',33.4),('3',78.6),('4',5.4),('5',45)]
l1=[t[l] for t in 1]
l1.sort(reverse=True)
#print(l1)
l2=[()*len(l1)]
for tuple in l:
    idx = l1.index(tuple[1])
    l2[idx]=tuple
print(l2)

