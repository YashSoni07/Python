import sys

print(sys.getrecursionlimit())
print(sys.setrecursionlimit(200))

i = 0
def a1():
    global i
    i = i + 1
    print("A1 functions", i)
    a1()
a1()

print(sys.getrecursionlimit())