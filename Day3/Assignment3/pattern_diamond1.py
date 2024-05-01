n= int(input("Enter no. of lines->>"))
count=0
stars=1
spaces= n//2
while(count < (n//2 +1)):
     print(" "*spaces,"*"*stars,sep="")
     spaces=spaces-1 #spaces-=1
     stars= stars+2 #stars+=2
     count+=1

stars=n-2
spaces=1
while(count>1):
     print(" "*spaces,"*"*stars,sep="")
     spaces=spaces+1 #spaces-=1
     stars= stars-2 #stars+=2
     count-=1