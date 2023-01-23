#HOD
# With one Function
def a1(P1):
    return "Hello", P1()
def a2():
    return "Hy"
print(a1(a2))

# With Tow Parameter
def a1(P1, P2):
    return "Hello", P1(), P2()
def a2():
    return "Hy"
def a3():
    return "Hi"
print(a1(a2, a3))