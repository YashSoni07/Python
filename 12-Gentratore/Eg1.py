# 1.
def a1():
    return 10
    return 20


a = a1()
print(a)
print(type(1))


# 2.
def a2():
    yield 1  # The yield statement can be used to omit the parentheses that would otherwise be required in the equivalent yield expression statement.
    yield 2
    yield 3


aa = a2()
print(type(aa))  # <class 'generator'>
print(next(aa))
print(next(aa))
print(next(aa))


print(next(aa)) #StopIteration


# 3.
def a1(n):
    for i in range(n):
        yield i


a = a1(5)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) # StopIteration
