from datetime import date
import time

d = []
d1 = date(2017, 8, 12)
d2 = date(2017, 6, 12)
d3 = date(2017, 4, 12)
d4 = date(2017, 5, 12)

d.append(d1)
d.append(d2)
d.append(d3)
d.append(d4)

d.sort(reverse=False)  # Sort in sequence order

for i in d:
    print(d)