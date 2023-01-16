# frozenset
f1 = frozenset([1, 2, 3, 4, 5])
print(f1)

s1 = {10, 20, 30, 40, 50}
s1.add(f1)
print(s1)  # {frozenset({1, 2, 3, 4, 5}), 50, 20, 40, 10, 30}
s1.remove(f1)
print(s1)
