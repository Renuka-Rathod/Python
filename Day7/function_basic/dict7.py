#Q WA function to take a dictionary as parameter. Print value of key "name" if key "rollno" is having value 100.
def print_name_for_roll_100(dictionary):
    if "rollno" in dictionary and dictionary["rollno"] == 100:
        print(dictionary.get("name", "Key 'name' not found or value is None"))
        
my_dict1 = {"rollno": 100, "name": "John"}
print_name_for_roll_100(my_dict1)  # Output: John

