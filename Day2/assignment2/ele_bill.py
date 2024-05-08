"""Write a program to calculate the electricity bill (accept number of unit from user) 
according to the following criteria :  
             Unit                                    Price    
First 100 units                                       no charge  
Next 100 units                                        Rs 5 per unit  
After 200 units                                       Rs 10 per unit  
(For example if input unit is 350 than total bill amount is Rs2000) """
unit=int(input("accept number of unit from user:"))
#print(unit)
if 0<unit<100:
   price=0
   print("price will be zero")
elif 100<unit<=200:
    nunit=unit-100
    price=5*nunit
    print(price)
elif  unit>200:
    price=100*5
    munit=unit-200
    nprice=munit*10
    total = price+nprice
    print(total)





