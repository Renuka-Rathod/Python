#720
rupees=int(input("Enter the amount:->"))
note=[2000,500,100,50,10,5,2,1 ]
for i in note:
    if(rupees>i):
        count=rupees//i
        rupees=rupees%i
        print(i,"=",count)

