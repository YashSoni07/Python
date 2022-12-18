# Slicing
# Sintext = slicing [start: end(-1) : step-over(1)]

l1 = [10,20,30,40,50,60,70,80,90,100]
#      1  2  3  4  5  6  7  8  9  10
#     -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(len(l1))
print(l1[0:6:])
print(l1[2:8:1])
print(l1[2:12:2])

print(l1[::])
print(l1[::2])
print(l1[:6:])
print(l1[4::])

print(l1[::-1])
print(l1[-10])
# print(l1[2:9:-1]) #TypeError: 'builtin_function_or_method' object is not subscriptable

