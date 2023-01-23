import datetime

# datetime.date(year, month, day)Creates a local date explicitly
d = datetime.date(2021,8,20)
print(d)
print(d.year, d.month, d.day)
print(d.today())
print(d.__class__)  # <class 'datetime.date'>

# Today date -- returns the locale date implicitly
t = datetime.datetime.today()
print(t.today())
print(t.day, t.month, t.year)
print(t.hour, t.minute, t.second)
print(t.__class__)

# Set Year, Month, Day
d = datetime.date(2021,8,30)
print(d)

# Set Hour, Minute
t1 = datetime.time(10,45)
dt = datetime.datetime.combine(d,t1)
print(dt)

