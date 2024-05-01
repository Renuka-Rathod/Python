"""Write a program to check whether an years is leap year or not the year is leap if it satisfies following 
condition It the year is divisible by 100 o If it is divisible by 100, then it should also be divisible by 
400 then it is leap year otherwise, all other years divisible by 4 and not divisible by 100
 then it is leap year. """

year= int(input("Enter the year:"))
print(year)

if(year%100==0 and year%400==0) or (year%4==0 and year!=100):
   print("year is a leap.")
else:
   print("year is not a leap.")