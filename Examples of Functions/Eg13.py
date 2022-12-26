def d1():
    a = 100
    b = 200
    print(a, b)
    print(locals()['a'] , locals()['b'])
    locals()['a']= 10
    locals()['b']= 20
d1()