import pandas as p

l1 = [10, 20, 30, 40, 50]
print(p.Series(l1))

l2 = [10, 20, 30, 40, 50]
print(p.Series(l2, index=['A', 'B', 'C', 'D', 'E']))

