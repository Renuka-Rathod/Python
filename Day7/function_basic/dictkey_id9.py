#Q WA function to take list of dictionaries. Print all dictionaries which contain key "id".
def print_dicts_with_id(lst):
    for d in lst:
        if "id" in d:
            print(d)
my_list = [
    {"name": "John", "id": 1},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "id": 2, "age": 30},
    {"name": "Charlie", "age": 35}
]
print_dicts_with_id(my_list)  # Output: {'name': 'John', 'id': 1}, {'name': 'Bob', 'id': 2, 'age': 30}
``