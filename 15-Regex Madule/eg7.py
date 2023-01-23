import re

string = 'hello 007 welcome to home'
pattern = r'\d+'  # d+ is used to print the number
r = re.findall(pattern, string)
print(r)

string = 'hello 007 welcome to home'
pattern = r'\w+'  # w+ is used to print the hole string
r = re.findall(pattern, string)
print(r)