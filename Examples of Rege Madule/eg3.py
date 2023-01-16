# To print the

import re
string = 'YashSoni@gmail.com'
pattern = r'(\w+)@(\w+).(\w+)'
r = re.match(pattern, string)
print(r)
print(r.group(0))  # YashSoni@gmail.com
print(r.group(1))
print(r.group(2))
print(r.group(3))
# print(r.group(4)) # IndexError: no such group
print(r.group(1, 2, 3))
