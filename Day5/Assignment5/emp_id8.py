emp_name, emp_id = input("Enter Emp_name and Emp_id separated by ':' -> ").split(':')

if int(emp_id) ** 0.5 % 1 == 0:  
    vowels = 'aeiouAEIOU'
    result = ''.join(c for c in emp_name if c in vowels)
elif all(int(emp_id) % i != 0 for i in range(2, int(emp_id) // 2 + 1)):  
    result = ''.join(emp_name[i] for i in range(len(emp_name)) if i % 2 == 0)
elif int(emp_id) % 2 != 0:  
    result = sum(ord(c) for c in emp_name)
else:
    result = None

print(result)
