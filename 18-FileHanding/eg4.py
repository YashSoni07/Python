# f = open('one.txt', 'r')
# print(f.tell())
# print(f.read())
# print(f.tell())

# f = open('one.txt', 'r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# print(f.read())

f = open('one.txt', 'r')
print(f.tell())
print(f.read(5))
print(f.tell())
f.seek(5)
print(f.read())