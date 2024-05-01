"""s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan
"""
s1 = "America"
s2 = "Japan"
#s3=len(s1)//2
s3= s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+ s1[-1]+s2[-1]
print(s3)
