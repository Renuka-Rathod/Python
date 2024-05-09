# n=5
# sp=0
# for idx in range(n-1,-1,-1):
#     print(" "*sp,'10'*idx,'1',sep="")
#     sp = sp+1

n=5
sp=(n//2)+1
for idx in range(1,n-1,1):
    print(" "*sp,'10'*idx,'1',sep="")
    sp = sp-1