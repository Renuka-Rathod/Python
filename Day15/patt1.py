# u = int(input("Enter a num - "))

# for n in range(u,0,-1):
#     print("10"*(u-1),end="")
#     u -= 1
#     print("1")

# u = int(input("Enter a num - "))

# space = 0
# for n in range(u,0,-1):
#     print("_"*space,end="")
#     print("10"*(n-1),end="")
#     print("1")
#     space += 1
"""enter a row count:5
*
**
***
****
*****"""
row = int(input("enter a row count:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")

