# To print the full String
import re
string = 'HelloYash'
pattern = r'\w+'  # + mein Numbers of occurrence
r = re.match(pattern, string)
print(r)
print(r.group())

# It will only accept a-z , A-Z, _ , 0-9
string = 'Hello_Yash-Soni'
pattern = r'\w+'
r = re.match(pattern, string)
print(r)
print(r.group())
