# Decorator
def a1(func):
    def a2():
        return "Hello", func()
    return a2

# WithOut Decorator
def a3():
    return "World"
c = a1(a3)
print(c())

# With Decorator
@a1
def a4():
    return "WORLD"
print(a4())
