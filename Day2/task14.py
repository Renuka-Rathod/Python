"""Problem 12:Write a program to print whether a given number is a prime number or not"""

no = int(input("Enter a no"))
idx=2
while(idx < (no)):
    if (no % idx) == 0:
        print("not a prime")
        break 
    idx +=1
else:
    print("Prime")

