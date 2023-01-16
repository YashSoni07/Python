# globals () and local()
# outside values are also coming in side

a = 10
b = 20
def a1():
    a = 10.0
    b = 20.0
    print('Local', a, b)
    print('Before: ', globals()['a'], globals()['b'])
    globals()['a']= 10
    globals()['b'] = 20
    print('After: ', globals()['a'], globals()['b'])
a1()
