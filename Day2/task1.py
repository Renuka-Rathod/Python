"""Problem 1: Write a program that will give you in hand monthly salary after deduction 
on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%"""

# Input CTC from the user
ctc = float(input("Enter your Cost to Company (CTC) in lakhs: "))

# Calculate deductions
hra = 0.10 * ctc
da = 0.05 * ctc
pf = 0.03 * ctc

# Calculate taxable income after deducting HRA, DA, and PF
taxable_income = ctc - hra - da - pf

# Determine tax bracket and calculate tax deduction
if taxable_income <= 500000:
    tax_rate = 0
elif 500000 < taxable_income <= 1000000:
    tax_rate = 0.10
elif 1000000 < taxable_income <= 2000000:
    tax_rate = 0.20
else:
    tax_rate = 0.30

tax_deduction = tax_rate * taxable_income

# Calculate net monthly salary
net_salary = ctc - hra - da - pf - tax_deduction

# Print net monthly salary
print("Net Monthly Salary: {:.2f} lakhs".format(net_salary))
