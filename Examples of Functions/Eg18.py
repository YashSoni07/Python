# Outer Functions OR Inner Functions Higher Order Function(HOD)
def outerFunction(a, b):
    print(a,b)

    def innerFunction(c, d):
        print(c, d)

    return innerFunction

# in this fist you have to take permission  form the parent
father = outerFunction(3,4)
print(father.__name__) # innerFunction
father(3, 4)