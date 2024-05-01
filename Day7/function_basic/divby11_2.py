#Q WA function to take list as parameter and print all numbers of given list which are divisible by 11
def divisible_by_11(list):
    
    divisible_numbers = [num for num in list if num % 11 == 0]

    for num in divisible_numbers:
        print(num)
my_list = [21, 33, 44, 51, 66, 77, 88, 99, 100, 121]
divisible_by_11(my_list)
