#open  a file and count frequency of every word in the file
#simple open and close(not recommended)
f = open("sample_file.txt")
print(f.read())
f.close()

#with construct(recommended)
with open("sample_file.txt") as f:
    #do the file operations inside with construct
    print(f.read())
print("outside with..file will be closed automatically")
print(f.read()) #exception