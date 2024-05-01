"""s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt
"""
s1 = "Ault"
s2 = "Kelly"
s3=len(s1)//2
s3=s1[:s3] + s2 + s1[s3:]
#print(s1[])
print(s3)
