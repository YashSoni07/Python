# Outer Functions OR Inner Functions
def outerFunction():
    print("Outer Function")
    def innerFunction():
        print("Inter Function")
    innerFunction()

outerFunction()