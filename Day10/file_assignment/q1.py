#1. Write a Python program to read an entire text file.
f = open("q1.txt")
print(f.read())
f.close()

#with construct(recommended)
with open("q1.txt") as f:
    #do the file operations inside with construct
    print(f.read())
print("outside with..file will be closed automatically")
print(f.read()) #exception