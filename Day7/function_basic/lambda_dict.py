
users = [
    {
        'name':'rahul',
        'age':5
    },
    {
        'name':'rutu',
        'age':90
    },
    {
        'name':'revti',
        'age':40
    }


]
d=tuple(map(lambda users:users['age'],users))
print(d)

g=[(2,1),(3,2),(4,3),(7,4),(8,5)]
z=sorted(g,key=lambda  x:x[1])
print(z)