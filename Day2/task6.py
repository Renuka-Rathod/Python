"""Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding
 up the two numbers before it. The first two numbers are 0 and 1. 
 For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series 
 above is 13+21 = 34"""


# Initialize the first two terms of the Fibonacci series
a = 0
b = 1

# Print the first two terms of the Fibonacci series
print(a)
print(b)

# Loop to generate the next 8 terms of the Fibonacci series
for _ in range(8):
    c = a + b  # Calculate the next term
    print(c)   # Print the next term
    a = b      # Update the values for the next iteration
    b = c

    