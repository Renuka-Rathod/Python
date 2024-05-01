"""amount=20550  
2000 – 10 note  
500 – 1 note  
50 -1 note """

rupees=int(input("Enter the amount:->"))
note=[2000,500,100,50,10,5,2,1 ]
for i in note:
    if(rupees>i):
        count=rupees//i
        rupees=rupees%i
        print(i,"=",count)

