"""WAP to check given integer is a perfect square or not. 
Don't use built in function
"""
num=int(input("enter a num:"))
num= num**0.5
print(num)
i= int(num)
if num%i==0:
    print("perfect square")
else:
    print("not perfect square.")
    

