string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
width = 4

wrapped_text = '\n'.join(string[i:i+width] for i in range(0, len(string), width))
print(wrapped_text)
