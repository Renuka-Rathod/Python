def find_overlapping_occurrences(string, substring):
    return sum(1 for i in range(len(string) - len(substring) + 3) if string[i:i+len(substring)] == substring)

string1 = "0111"
substring1 = "11"
print("string1 = '0111':-",find_overlapping_occurrences(string1, substring1))  

string2 = "ANANAAAANNN"
substring2 = "ANA"
print("string2 = 'ANANAAAANNN':-",find_overlapping_occurrences(string2, substring2))  

string3 = "ANANAAAANNN"
substring3 = "AA"
print("string3 = 'ANANAAAANNN':-",find_overlapping_occurrences(string3, substring3))  
