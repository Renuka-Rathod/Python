L1=[1,1,2,3,2,3,4,5,4]
L2=[1,2,3,3,2]
L=[]
for i in L2:
    if i not in L:
        L.append(i)

print(L)
