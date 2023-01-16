import re

p = r'(Wild.*)'  # .* Is used to print the next elements
s = 'Animals live in forest called Wild Animals etc...'
r = re.search(p, s)
print(r.group())

p = r'(^A)'  # .^ Is used to print the First elements
s = 'Animals live in forest called Wild Animals etc...'
r = re.search(p, s)
print(r.group())

p = r'(Soni$)'  # .$ Is used to print the list elements
s = 'YashSoni'
r = re.search(p, s)
print(r.group())
