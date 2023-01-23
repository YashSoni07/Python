# To Find How many Days you Lived?

import datetime

# Orginal date
t = datetime.datetime.today()
print(t)

# Replace date
start = t.replace(year=2000, month=12, day=24)
print(start)

end = datetime.datetime(year=2023, month=1, day=23)
print(end)

d = end - start
print(d.days)  # days is a property , 8064
