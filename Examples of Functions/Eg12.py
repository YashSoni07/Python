# globals () and local()
a = 10
b = 20
def d1():
    a = 100
    b = 200
    print('Local', a, b)
    print(globals()['a'], globals()['b'])
    globals()['a']= 30
    globals()['b'] = 40
    print(globals()['a'], globals()['b'])
d1()
