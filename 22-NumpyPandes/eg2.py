from numpy import *

# lin-space(start, stop)

l1 = linspace(1.0, 5.0)
print(l1)

# lin-space(start, stop, num)

l2 = linspace(1.0, 5.0, retstep=True)
print(l2)

l3 = linspace(1.0, 5.0, retstep=False)
print(l3)

l4 = linspace(1, 10, num=10, endpoint=True)
print(l4)

l5 = linspace(1, 10, num=10, endpoint=True, retstep=True)
print(l5)

l6 = linspace(1, 10, num=10, endpoint=True, retstep=False)
print(l6)
