def a1(a,b):
    while a<=b:
        yield a
        a=a+1

a = a1(1,5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) #StopIteration