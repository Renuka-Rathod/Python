"""accept amount from user and find the minimum number
 notes required to get the amount amount =512  
Notes: 2000,500,100,50,10,5,2,1 """

rupees=int(input("Enter the amount:"))
notes=[2000,500,100,50,10,5,2,1]
for i in notes:
    if (rupees>i):
        count=rupees//i
        rupees=rupees%i
        print(i,"=",count)
        continue
        

