"""12. Take integer from user and print all odd numbers which can be generated using any number of digits
 from given number
Ex. 
Input: 3421  o/p: 1,3,13,43,23,31,41,21,421,241,341,431,423,243,143,413,1243,1423,4213,4123, 2413,2143, .. etc
"""
# Take input from the user
num = int(input("Enter an integer: "))

# Convert the number to a string
num_str = str(num)

# Iterate through each digit in the number
for i in range(len(num_str)):
    # Check if the digit is odd
    if int(num_str[i]) % 2 != 0:
        # Initialize a string to store odd numbers
        odd_numbers = ""
        # Iterate through the digits starting from the current digit
        for j in range(i, len(num_str)):
            # Append the current digit to the string
            odd_numbers += num_str[j]
            # Check if the number formed by the digits is odd
            if int(odd_numbers) % 2 != 0:
                print(odd_numbers)  # Print the odd number

