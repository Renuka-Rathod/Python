import re

text = "this is a good number 9089786756 and 8900000000 is a desired number"
mobile_numbers = re.findall(r'\b\d{10}\b', text)

print(", ".join(mobile_numbers))

