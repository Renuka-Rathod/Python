"""s1 = "Abc"
s2 = "Xyz"
Expected Output:
AzbycX
"""
s1 = "Abc"
s2 = "Xyz"
s3=s1[0]+s2[-1]+s1[1]+s2[1]+s1[-1]+s2[0]
print(s3)