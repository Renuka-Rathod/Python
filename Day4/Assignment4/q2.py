"""2. take a list 'l1' of even nos between 150 to 250. Print its length.
Then create another list 'l2' using 'l1', containing only nos divisible by 4 from 'l1'."""
l1 = [e for e in range(150, 251) if e % 2 == 0]
print("Length of l1:", len(l1))
l2 = [num for num in l1 if num % 4 == 0]
print("list is:", l2)