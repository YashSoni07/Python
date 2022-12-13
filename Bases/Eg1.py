# create empty list
L1 = list()
print(L1)

L2 = []
print(L2)

# list [Elements]
L3 = [list,float,str]
print(L3)

L4 = [list(),float(),str()]
print(L4)

# list contains duplicates , insertion order preseverd / ordered elements
L1 = [10 , 20 , 30 , 40 , 50 , 10 , 20 , 30 , 40 , 50]

print(L1)

L2 = [id(L1[1])] , [id(L1[6])]
print(L2)

# add two list
list1 = [10 , 20 , 30  ]
list2 = [40 , 50 , 60 ]
print(list1+list2)

# multiply
l1 = [50 , 60 , 70  ]
print(l1*3)
