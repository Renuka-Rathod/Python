"""Problem 3: Write a program that will take user input of cost price and selling price 
    and determines whether its a loss or a profit."""

cost_price=float(input("Enter cost price valuse:"))
selling_price = float(input("Enter selling price value:"))
if selling_price-cost_price>0:
    print("Its profit")
else:
    print("It's loss")