#lambda function
#x -> x^2
a = lambda x : x**2
print(a(2))

x= lambda l,m : l+m 
print(x(2,3))

s = lambda a : 'k' in a
print(s('string'))

#odd or even
z = lambda e : 'even' if e%2==0 else 'odd'
print(z(8))

z=lambda a,b,c :a+b+c
print(z(2,3,5))