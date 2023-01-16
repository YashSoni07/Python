# Outer Functions OR Inner Functions Higher Order Function(HOD)
def a1(a):
    def a2(b):
        return a+b
    return a2
A= a1(10)
print(A(10))