#Q WA function to take list of strings as parameter and print all strings which have character 's' 2 times

def print_strings_with_two_s(lst):
    for string in lst:
        if string.count('s') == 2:
            print(string)
my_list = ["apple", "banana", "grapes", "orange", "passionfruit", "strawberry", "passport","kiwi", "cassis"]
print_strings_with_two_s(my_list)  # Output: passport, passionfruit
