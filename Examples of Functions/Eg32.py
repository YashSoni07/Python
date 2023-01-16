# WithOut Lambda
def a1(a=5):
    def a2(b):
        return a+b
    return a2
a = a1(10)
print(a)
print(a(5))

# With Lambda
a1 = lambda a=5: lambda b: a+b
a= a1(10)
print(a(5))