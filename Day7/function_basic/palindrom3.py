#Q WA function to take string as parameter
#Check if string is palindrome or not If palindrome return 1 if not palindrome return 0

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
s = input("Enter a string: ")
if is_palindrome(s):
    print(1)
else:
    print(0)
