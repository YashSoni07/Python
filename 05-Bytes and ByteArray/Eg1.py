b1 = bytes()
print(b1)

b2 = bytes([1, 2, 3, 4, 5])
print(b2)

b3 = bytearray()
print(b3)

b4 = bytearray([1, 2, 3, 4, 5])
print(b4) # b'\n\x14\x1e(2'

# b5 = bytes([1])
# b5[0] = 10
# print(b5) # TypeError: 'bytes' object does not support item assignment

b6 = bytearray([1])
b6[0] = 10
print(b6)