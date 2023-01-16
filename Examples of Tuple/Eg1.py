# Tuple
t1 = ()
print(t1)

# To create the empty tuple
t2 = tuple()
print(t2)

t3 = 10
print(type(t3))  # <class 'int'>

t3 = 10,
print(type(t3))  # <class 'tuple'>

t4 = 10, 20, 30, 40
t5 = (10, 20, 30, 40)
print(t4, t5)

# Immutable
t1 = (10, 20, 30, 40)
print(t1[0])

# t1[0] = 100
# print(t1) #TypeError: 'tuple' object does not support item assignment

t6 = [10, 20, 30, 40]
print(t6 * 2)

# t7 = [10,20,30,40]
# print(t6*t7) # TypeError: can't multiply sequence by non-int of type 'list'


t8 = [10, 20, 30, 40]
t9 = [50, 60, 70, 80]
print(t8 + t9)
