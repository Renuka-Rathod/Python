text = "Fgh^f #89"
space_count = text.count(" ")
special_char_count = sum(not char.isalnum() and not char.isspace() for char in text)

print("Spaces:", space_count)
print("Special characters:", special_char_count)
