# Multiply Iterables
l1 = [1, 2, 3, 4, 5]
l2 = [5, 4, 3, 2, 1]
# print(l1*l2) TypeError: can't multiply sequence by non-int of type 'list'

def a1(a,b):
    return a*b
result = map(a1, l1,l2)
print(result) # <map object at 0x00000272C435BE50>
print(list(result)) # [5, 8, 9, 8, 5]

# Map (Func (lambda a, b:a*b), Iterable( l1,l2)
print(list(map(lambda a, b:a*b, l1,l2))) # [5, 8, 9, 8, 5]