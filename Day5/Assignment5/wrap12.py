"""You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w 
example: String : “ABCDEFGHIJKLIMNOQRSTUVWXYZ”
Width: 4
Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
CODE--
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width = 4
wrapped_text = '\n'.join(string[i:i+width] for i in range(0, len(string), width))
print(wrapped_text)"""

string= "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width = int(input("Enter width:"))
for i in range(0,len(string),width):
    print(string[i:width+i])
