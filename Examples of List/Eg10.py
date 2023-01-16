# Deep copy and Shallow
# Deep copy operation on arbitrary Python objects. Is done by copy.deepcopy
# Shallow copy operation on arbitrary Python objects. Is done by copy.copy

import copy
# in deep copy the original list will not be affected
l1 = [[10, 20], [30, 40], [50, 60]]
print(len(l1))
l2 = copy.deepcopy(l1)

l1[0][0] = 100
print(l1)  # [[100, 20], [30, 40], [50, 60]]
print(l2)  # [[10, 20], [30, 40], [50, 60]]

print("----------")
# in shallow copy the original list will be affected
l1 = [[10, 20], [30, 40], [50, 60]]
print(len(l1))
l2 = copy.copy(l1)
l1[1][1] = 200
print(l1)  # [[10, 20], [30, 200], [50, 60]]
print(l2)  # [[10, 20], [30, 200], [50, 60]]
