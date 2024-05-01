#Q WA function to check if number is prime or not. Return True if number is prime and false if number not prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("True")
else:
    print("False")
