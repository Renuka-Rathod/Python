#sum of all items
import functools
l1=[1,2,3,4,5]
l2=[2,6,443,6]
h=list(map(lambda x:x+x,l1))
print(h)

#find min
# o=functools.reduce(lambda x,y:x if x<y else y,[1,2,45,67,897])
# print(o)