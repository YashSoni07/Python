import time

t1 = time.ctime()
print(t1)  # Sun Jan 22 23:08:12 2023
print(type(t1))  # <class 'str'>

t2 = time.localtime()
print(t2)
print(type(t2))  # <class 'time.struct_time'>

t3 = time.localtime()
print(t3.tm_year, t3.tm_mon, t3.tm_mday)

t4 = time.localtime()
print(t4.tm_isdst)
# ----------------------#

l1 = time.localtime()
print(type(l1))

# Abbreviated weekday name
r1 = time.strftime("%a", l1)
print(r1)

# Abbreviated weekday name
r2 = time.strftime("%A", l1)
print(r2)

# Abbreviated weekday name
r3 = time.strftime("%B", l1)
print(r3)

# Abbreviated month name
r4 = time.strftime("%b", l1)
print(r4)

# Hour (24hr) possible values 00 - 23
r5 = time.strftime("%H", l1)
print(r5)

# Hour (12hr) possible values 01 - 12
r6 = time.strftime("%I", l1)
print(r6)

# Day of the year possible values 001 -366
r7 = time.strftime("%j", l1)
print(r7)

# Month of the year possible values 01 - 12
r8 = time.strftime("%m", l1)
print(r8)

# %p either AM or PM
r9 = time.strftime("%p", l1)
print(r9)

# %w Weekday as decimal number , values from 0 to 6
r10 = time.strftime("%w", l1)
print(r10)

# %x for date representation
r11 = time.strftime("%x", l1)
print(r11)

# %X for time representation
r12 = time.strftime("%X", l1)
print(r12)

# %c date and time representation
r13 = time.strftime("%c", l1)
print(r13)

# %y year without date representation, values 00 -- 99
r14 = time.strftime("%y", l1)
print(r14)

# %Y year with century as decimal number
r15 = time.strftime("%Y", l1)
print(r15)

# %Z Time Zone Name
r16 = time.strftime("%Z", l1)
print(r16)
