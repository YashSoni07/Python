import re

# To find the latter
string = 'Yash'
pattern = r'Y'
r = re.match(pattern, string)
print(r)
print(r.group())

# To print fist latter of the string
string = 'Soni'
pattern = r'\w'  # by using \w you can print only one character and if you use \w\w the two character will print and
# so on
r = re.match(pattern, string)
print(r)
print(r.group())

