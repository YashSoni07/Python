# Arbitrary Arguments
def a1(*Colors):
    print(Colors)

a1('Red', 'black', 'blue', 'brown', 'white')

def a2(**Colors):
    print(Colors)
a2 (a = 10, b = 20, c = 30, d = 40)
