
"""Input 3421   : o/p max: 4321, min 1234
Input 7789    : o/p max: 9776   min 6779

"""
num = input("Enter a number: ")
min_num = int(''.join(sorted(num)))
max_num = int(''.join(sorted(num, reverse=True)))
print("max:", max_num, "min:", min_num)
