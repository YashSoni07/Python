# Using Comprehension
a = {i: i * i for i in range(1, 10)}
print(a)

# Using Constructor and Comprehension
a = dict((y, y * y) for y in range(1, 10))
print(a)

# Using Dict()
a = dict()
for y in range(1, 10):
    a[y] = y * y
print(a)
