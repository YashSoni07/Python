# Goble Keywords
a = 10
b = 20
def d1():
    global c
    global d
    c = 100
    d = 200
    print('Goble', a)
    print('Goble',b)
    print('local',c)
    print('Local',d)
d1()
print(c,d)
