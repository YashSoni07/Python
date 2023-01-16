def a1(a,b):
    if a>b:
        return a
    else:
        return b
a = a1(1, 2)
print(a)

a1 =lambda a, b : a if a>b else b
a= a1(1, 2)
print(a)