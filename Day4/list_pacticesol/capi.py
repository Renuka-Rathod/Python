sample="i am the confident girl in the world"
print(sample.split())
L=[]
for i in sample.split():
    print(i.capitalize())
    L.append(i.capitalize())
print(L)
print(" ".join(L))
