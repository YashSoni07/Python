# Closure
# if deleted the parent function then also the child function will work
def a1(a):
    print(a)
    def a2(b):
        print(b)
        return a2
c = a1(10)
print(a1(20))



