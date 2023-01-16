# Goble Keywords
a = 1
b = 2
def a1():
    global c
    global d
    c = 10
    d = 20
    print('Goble', a)
    print('Goble', b)
    print('local', c)
    print('Local', d)
a1()
print(c, d)
