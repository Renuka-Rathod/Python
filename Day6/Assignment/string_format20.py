#20. Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)
t1=(1,2,3)
print("this is tuple",str(t1))

t=(1,2,3)
tuple((*t[:2],4))
print(t)
