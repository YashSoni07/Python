def a1(a,b):
    def a2(c,d):
        return a+b, c-d
    return a2
A= a1(10,10)
print(A(10,10))
