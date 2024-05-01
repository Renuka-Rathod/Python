#Accept number from user and check whether it is divisible by 5 and 11 if divisible then display appropriate message.  
  
num = int(input("Enter any one number:=>"))
print(num)
if (num%5==0) & (num%11==0):
    print("num is div by 5.")
else:
    print("not div by 5 & 11.")