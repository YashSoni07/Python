# Direct Recursion
i = 0
def a1():
    global i
    i = i + 1
    print("A1 functions")
    a1()
a1()