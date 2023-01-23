# Goble and Local

a = 1
b = 2
def a1():
    a = 10
    b = 20
    print('Locals', a, b)
a1()
print('Global', a, b)
