# discard and remove
s1 = {1, 2, 3, 4, 5}
s1.remove(3)
print(s1)  # KeyError: 6

s2 = {1, 2, 3, 4, 5}
s2.discard(6)
print(s2)

# pop
s3 = {1, 2, 3, 4, 5}
print(s3.pop()) # 9
print(s3)
print(s3.pop()) # 3
print(s3.pop()) # 4
print(s3.pop()) # 1
print(s3.pop()) # 3
print(s3)