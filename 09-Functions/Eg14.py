a, b, c = 10, 20, 30
def a1():
    return globals()
print(a1())
def a2():
    x, y, z = 1, 2, 3
    return locals()
print(a2())