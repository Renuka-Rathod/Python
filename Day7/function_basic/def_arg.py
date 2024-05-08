#default argument
def power(a=1,b=1): #if nno value passed to b, by default it will consider as 1
    return a**b

x=power(3)#argument is value given to parameters
print(x)

#positional arguments
def power(x=1,y=1):
    return x**y
p=power(4,3)
print(p)

#keyword arguments
p1=power(y=3,x=2)
print(p1)

