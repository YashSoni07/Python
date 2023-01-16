# Iterables it is an object,
# It has two methods 1. Either method (.__iter__()) 2. is Next method (.__next__())

# one way
l1 = [1, 2, 3, 4, 5]
print(l1)
print(type(l1))
print(l1.__iter__()) # <list_iterator object at 0x0000027110F2BFA0>
l= l1.__iter__()
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
# print(l.__next__()) # StopIteration

# Second way
l2 = [1.0, 2.0, 3.0, 4.0, 5.0]
ll = iter(l2)
print(next(ll))
print(next(ll))
print(next(ll))
print(next(ll))
print(next(ll))
# print(next(ll)) # StopIteration