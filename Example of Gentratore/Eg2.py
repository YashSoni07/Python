a1 = {i for i in range(5)}
print(list(a1))
print(tuple(a1))
print(set(a1))

# casting

a2 = tuple(i for i in range(5))
print(a2)

a3 = set(i for i in range(5))
print(a3)

a4 = list(i for i in range(5))
print(a4)
