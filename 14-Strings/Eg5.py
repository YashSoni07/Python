# Find Method
a = 'Hello learners like code'
#    012345678........
print(a.find('l'))
print(a.rfind('l'))

print(a.find('l', 5, 9))

print(a.find('x'))  # when the latter is not in the list then it will show -1

# Reversed the list
b = 'HelleWorld'
print(list(reversed(b)))  # ['d', 'l', 'r', 'o', 'W', 'e', 'l', 'l', 'e', 'H']

for x in reversed(b):
    print(x, end=" ")  # d l r o W e l l e H