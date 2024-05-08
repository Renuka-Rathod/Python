#square the items of the list
a=list(map(lambda x : x**2,[1,2,3,6]))
print(a)

#odd/even labelling of the list items
L = [1,3,45,6,7,8]
m=list(map(lambda z : 'even' if z%2==0 else 'odd',L))
print(m)