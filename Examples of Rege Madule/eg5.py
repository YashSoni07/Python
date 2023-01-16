# To Find the element in String .search()

import re

p = r'(Wild Animals)'
s = 'Animals live in forest called Wild Animals etc...'
r = re.search(p, s)
print(r.group())
