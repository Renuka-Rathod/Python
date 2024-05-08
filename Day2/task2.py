"""Problem 2: Write a program that take a user input of three angles and 
will find out whether it can form a triangle or not."""
Angle1 = input("Enter angle1 of triangle:")
Angle2 = input("Enter angle2 of triangle:")
Angle3 = input("Enter angle3 of triangle:")


if Angle1+Angle2+Angle3==180:
    print("form a triangle.")
else:
    print("not formed a triangle.")