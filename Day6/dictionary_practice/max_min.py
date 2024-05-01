#15. Write a Python program to get the maximum and minimum values of a dictionary.
d = dict([(1,'val1'),[3.01,234],'ke'])
x1=int(input("Enter value of x1:"))
d={x:x for x in range(1,x1)}
print(d)
print('max:',max(d))
print('min',min(d))