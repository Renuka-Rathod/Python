# add two numbers

try:
    num1 = input("Enter a number")
    num1 = float(num1)
    num2 = input("Enter a number")
    num2 = float(num2)
except UnicodeError:
    print("Match UnicodeError")
except ValueError:
    print("There was error in format of the input.")
except:
    print("There is an exception")
else:
    print("addition is ", num1+num2)

print("Completed!!!")


"""
Enter a numberAA
Traceback (most recent call last):
  File "d:/Python_workshop/my_practice/exception_handling.py", line 4, in <module>
    num1 = float(num1)
           ^^^^^^^^^^^
ValueError: could not convert string to float: 'AA'
"""