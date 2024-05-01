#Q WA function to take a string as parameter. Print its alternate characters starting from 2nd character
def print_alternate_chars(string):
    alternate_chars = string[1::2]
    print(alternate_chars)
    
input_string = input("Enter a string: ")
print_alternate_chars(input_string)
