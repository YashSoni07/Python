print("Before")
try:
    a= 10
    b = 20
    c = 0
    print(a/b)
    print(a/c)
except ZeroDivisionError:
    print("ZeroDivisionError")
print("After")