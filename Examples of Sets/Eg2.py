print(dir(set))
# 'add',
# 'clear',
# 'copy',
# 'discard',
# 'pop',
# 'remove',
# 'update'

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(3.5)
s1.add(2)
s1.add(3.0)
print(s1)  # {1, 2, 3, 3.5}

s1 = {1,2}
s2 = {3,4}
# s1.add(s2)
# print(s1) # TypeError: unhashable type: 'set'
s1.clear()
s2.clear()
print(s1, s2)

# copy list and set
s1 = {1, 2}
print(s1.copy())
print(s1)
# print(s1*2) # TypeError: unsupported operand type(s) for *: 'set' and 'int'

l1 = [1, 2]
print(l1)
print(l1.copy())
print(l1*1)
print(l1[::])

