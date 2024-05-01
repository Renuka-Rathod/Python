"""Write a program to calculate the electricity bill (accept number of unit from user) 
according to the following criteria :  
             Unit                                    Price    
First 100 units                                       no charge  
Next 100 units                                        Rs 5 per unit  
After 200 units                                       Rs 10 per unit  
(For example if input unit is 350 than total bill amount is Rs2000) """

# Accept the number of units from the user
units = int(input("Enter the number of units consumed: "))

# Initialize the total bill amount
total_bill = 0

# Calculate the bill based on the criteria
if units <= 100:
    # No charge for the first 100 units
    total_bill = 0
elif units <= 200:
    # Rs 5 per unit for the next 100 units
    total_bill = (units - 100) * 5
else:
    # Rs 10 per unit for units beyond 200
    total_bill = (100 * 5) + (units - 200) * 10

print(f"Total bill amount: Rs {total_bill}")
