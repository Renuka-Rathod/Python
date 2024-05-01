count=0
num=int(input("Enter an int"))
while(num>0):
    d=num%10
    print("next digit is",d)
    count+=1
    d=d//10

num=input("Enter an int")
print("count of digits",len(num))
print("count of digits",num[len(num)-1])
print("count of digits",num[0])