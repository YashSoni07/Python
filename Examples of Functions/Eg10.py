#Goble and Local

a = 10
b = 20
def d1():
    a = 100
    b = 200
    print('Locals', a, b)
d1()
print('Global', a, b)
