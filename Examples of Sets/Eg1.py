# empty set
s1 = set()
print(s1)

# insertion order is not preserved/Unordered, duplicates not allowed
# data structures hashcode
s1 = {1, 2, 3, 4, 2, 4, 5, 6, 7}
print(s1) # {5, 2, 7, 4, 1, 6, 3}

# data structures index positions
l1 = [1, 2, 3, 4, 2, 4, 5, 6, 7]
print(l1)

# remove duplicate elements using list
l1 = [1, 2, 3, 4, 2, 4, 5, 6, 7, 1, 2]
print(set(l1))

a = 1
b = 1.0
print(type(a), type(b))
print(a == b) # content comparison