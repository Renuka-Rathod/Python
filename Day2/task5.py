# menu driven calculator
print("""
Hi how can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit
""")
menu = int(input("Enter your choice:"))
if menu == 1:
  print("pin change")
elif menu == 2:
  print("balance")
elif menu == 3:
  print("withdrawl")
else:
  print("exit")