# Indirect Recursion
def a1():
    print('A1 Function')
    a2()

def a2():
    print('A2 Function')
a1()