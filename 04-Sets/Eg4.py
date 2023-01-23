# Update a set with the union of itself and others. By using (.update)
s1 = {10, 20, 30, 40, 50}
print(s1)  # Before
s1.update([1, 2, 3, 4, 5])
print(s1)  # After

s2 = {'A', 'B', 'C', 'D'}
print(s2)
s3 = {'a', 'b', 'c', 'd'}
s3.update(s2)
print(s3)

s4 = {1, 2, 3, 4, 5, 6, 7, 8}
l1 = list(s4)
print(l1)
print(l1[0])

# list
l1 = ["Yash", "Harsh", "Shashwat", "Kapil"]
print(set(l1))

