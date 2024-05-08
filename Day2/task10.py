"""Problem 10: Write a program that keeps on accepting a number from the user until
 the user enters Zero. Display the sum and average of all the numbers."""
total = 0
count = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    
    total += num
    count += 1

if count != 0:
    average = total / count
    print("Sum:", total)
    print("Average:", average)
else:
    print("No numbers were entered.")

