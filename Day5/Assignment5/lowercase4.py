"""Given an input string with the combination 
of the lower and upper case arrange characters 
in such a
way that all lowercase letters should come first."""

#input_string = "AbCdEfGhIjKlMnOpQrStUvWxYz"
input_string=str(input("Enter String:"))
print("Given String is:-",input_string)
lowercase_letters = [char for char in input_string if char.islower()]
uppercase_letters = [char for char in input_string if char.isupper()]

arranged_string = ''.join(lowercase_letters + uppercase_letters)

print(arranged_string)
