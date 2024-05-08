#Q WA function to take a number as parameter and  print True if given number is even else print False

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("True")
# else:
#     print("False")

def is_even(num):#here num is parameter
    """
    This function returns num is odd or even
    """
    if type(num)==int:
        if num%2==0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'pagal hai kya?'
    
for i in range(1,5):
    x=is_even(i)#argument
    print(x)
    
