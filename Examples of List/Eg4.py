# Index
l1 = [10,20,30,40,50]
#      0  1  2  3  4
print(len(l1))
print(l1.index(40))

l2 = ['A', 'B', 'C', 'D', 'E']
#      0     1    2    3    4
print(len(l2))
print(l2.index('C'))

l3 = [10,20,30,40,50,40,30,20,10,50]
#      1  2  3  4  5  6  7  8  9  10
print(l3.index(20))
print(l3.index(20,7,9)) # index(element, start, stop)


