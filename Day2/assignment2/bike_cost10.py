"""10. Write a program to accept the price of a bike and display the road tax and insurance
 to be paid according to the following criteria . also display total amount to be paid.  
      
        Cost price (in Rs)           Tax                Inssurance  
        > 100000                     15 %                   20%  
        > 50000 and <= 100000        10%                    8%  
        <= 50000                     5%                     5% """
 
cost_price=float(input("Enter the bike price(in Rs.):"))
print(cost_price)
if cost_price>100000:
    tax_per=15
    inssurance_per=20
elif 50000<cost_price<=100000:
    tax_per=10
    inssurance_per=8
else:
    tax_per=5
    inssurance_per=5
tax_amount=(tax_per/100)*cost_price
inssurance_amount=(inssurance_per/100)*cost_price
total_amount=cost_price+tax_amount+inssurance_amount
print("Road tax:",tax_amount)
print("insurrance amount(in Rs.):",inssurance_amount)
print("total amount to be paid(in Rs.):",total_amount)

