# Creating Empty List
l1 = list()
print(l1)

l2 = []
print(l2)

# List [Elements]
l3 = [int, float, str, complex, bool, list, set, dict, tuple, range, bytes, bytearray, frozenset]
print(l3)

l4 = [int(), float(), str(), complex(), bool(), list(), set(), dict(), tuple(), range(0), bytes(), bytearray(),
      frozenset()]
print(l4)

# List contains duplicates , insertion order preserved / ordered elements
l1 = [10, 20, 40, 50, 20, 40, 50, 20, 40, 50]
#      0  1  3  4  5  6  7  8  9 10
print(l1)

# id()
l2 = [id(l1[1]), id(l1[5]), id(l1[8])]
print(l2)

# add to list (Happens concat)
l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 40, 50]
print(l1 + l2)

# Multiplying the list with any no
print(l1 * 2)

# Multiplying the list with list
# print(l1*l2) # TypeError: can't multiply sequence by non-int of type 'list'


print(dir(list))
