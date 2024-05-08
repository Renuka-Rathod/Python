"""Problem 10: Write a program, which will find all such numbers between 1000 and 3000 
(both included) such that each digit of the number is an even number. The numbers 
obtained should be printed in a space-separated sequence on a single line."""
"""
for i in range(999,3001):
    if i%2==0:
        print(i,end=" ")
        """

for i in range (1000,3001):
    i=str(i)
    leng=len(i)
    l=[]
    for j in i:
        l.append(j)
    #print(l)

    count=0
    for k in l:
        
        if int(k)%2==0:
            count=count+1
    #print(count)
    #print(leng)

    if count==leng:
        print(i , end=" ")
    