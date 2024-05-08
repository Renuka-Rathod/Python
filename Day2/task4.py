# Menu-driven program
print("""
1. cm to ft
2. km to miles
3. USD to INR
4. Exit
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("cm to ft")
elif choice == 2:
    print("km to miles")
elif choice == 3:
    print("USD to INR")
elif choice == 4:
    print("Exiting the program")
else:
    print("Invalid choice. Please enter a number from 1 to 4.")
