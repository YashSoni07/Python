# WithOut Lambada Function
def a1(a=1, b=2):
    return a+b
a = a1()
print(a)

# With Lambada Function
a1 = lambda a=1, b= 2: a+b
a = a1()
print(a)
