# # Multiply Iterables
# l1 = [1, 2, 3, 4, 5]
# print(l1 * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#
# # For Loop and Lambda
# l1 = [1, 2, 3, 4, 5]
# l = []
# a = lambda n: n * 2
# for i in l1:
#     l.append(a(i))
# print(l)  # [2, 4, 6, 8, 10]
#
# # Map (Func, Iterable)
# l1 = [1, 2, 3, 4, 5]
#
#
# def a1(n):
#     return n * 2
#
#
# a = map(a1, l1)
# print(a)  # <map object at 0x0000026DD08BBEE0>
# print(list(a))  # [2, 4, 6, 8, 10]
#
# # Map (Func (lambda n: n*2), Iterable ([1, 2, 3, 4, 5]))
# print(list(map(lambda n: n * 2, [1, 2, 3, 4, 5])))  # [2, 4, 6, 8, 10]

d1 = {1: 10, 2: 20}
d2 = {'a': 'apple', 'b': 'boll'}
d1.update(d2)
print(d1)



