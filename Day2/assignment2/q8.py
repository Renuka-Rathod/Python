#Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.  

num = int(input("Enter a number."))
print(num)
last_digit = num %10

if(last_digit%3==0):
    print("div by 3")
else:
    print("not div by 3")