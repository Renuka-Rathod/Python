"""Take integer from user and print all odd numbers which can be generated 
using any number of digits from given number
Ex. 
Input: 3421  o/p: 1,3,13,43,23,31,41,21,421,241,341,431,423,243,143,413,1243,1423,4213,4123, 2413,2143, .. etc
"""
num = input("Enter a number: ")

odd_nums = []


for i in range(len(num)):
    for j in range(len(num)):
        if i != j:
            new_num = num[:i] + num[j]

            if int(new_num) % 2 != 0:
                
                odd_nums.append(new_num)


print("Odd numbers:", ', '.join(odd_nums))

