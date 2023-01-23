# Outer Functions OR Inner Functions
def outerFunction(a, b):
    print("Outer Function", a, b)
    def innerFunction(c, d):
        print("Inter Function", c, d)
    innerFunction(1,2)

outerFunction(3,4)
