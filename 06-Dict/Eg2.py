# To add one dict date to another dict by .update
d1 = {1: 10, 2: 20, 3: 30, 4: 40}
d2 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
d2.update(d1)
print(d2)

d1 = {1: 10, 2: 20, 3: 30, 4: 40}
d1.update({5: 50})

d1 = {1: 10, 2: 20, 3: 30, 4: 40}
d1.update({3: 300})
