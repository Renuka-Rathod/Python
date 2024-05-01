#Q Sort all the characters of given string using lambda function

words=["hi","hello","welcome","wonderful"]
print(sorted(words,key=lambda s:s[1]))   #o/p: ['hello', 'welcome', 'hi', 'wonderful']
