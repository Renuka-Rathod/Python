"""Q Sort all the numbers in a list in descending order using lambda function
sorted(l1, key=(lambda x:-x))
"""
l1= [2,4,5,2,8,9,-2]
print(sorted(l1, key=(lambda x:-x)))