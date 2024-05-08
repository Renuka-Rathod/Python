#numbers greater than 5
l=[3,6,0,9,123]

a=list(filter(lambda x:x>5,l))
print(a)

#fetch fruits starting with 'a
fruits = ['apple','peru','banana','aloo']
f=list(filter(lambda x: x.startswith('a'),fruits))
print(f)