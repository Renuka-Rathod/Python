
def middle_three_chars(s):
    mid_index = len(s) // 2
    middle_chars = s[mid_index - 1:mid_index + 2]
    
    return middle_chars
str1 = "RakeshzipPetabb"
str2 = "JazzbonAyxx"


print(middle_three_chars(str1))  
print(middle_three_chars(str2))  

